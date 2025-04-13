from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class MyGameOffer(models.Model):
    _name = 'mygame.offer'
    _description = 'Game Price Offer'

    game_id = fields.Many2one('mygame.game', string='Game', required=True, ondelete='cascade')
    offered_price = fields.Float(string='Offered Price', required=True)
    partner_id = fields.Many2one('res.partner', string='Offered By', required=True)
    offer_date = fields.Datetime(string='Offer Date', default=fields.Datetime.now)
    
    
    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res_user = self.env.user
        if 'partner_id' in fields and res_user.partner_id:
            res['partner_id'] = res_user.partner_id.id
        return res

    @api.model
    def create(self, vals):
        game = self.env['mygame.game'].browse(vals['game_id'])
        if game.is_sold:
            raise ValidationError(_("این بازی قبلاً فروخته شده و نمی‌توان برای آن آفر ثبت کرد."))

        record = super().create(vals)

    # افزودن سازنده بازی به دنبال‌کنندگان
        if game.create_uid:
            game.message_subscribe(partner_ids=[game.create_uid.partner_id.id])

    # ارسال نوتیفیکیشن
        game.message_post(
            body=_("کاربر %s برای بازی شما آفر جدیدی به مبلغ %s$ ثبت کرد.") % (
                record.partner_id.name, record.offered_price),
            subject=_("آفر جدید برای بازی %s") % game.game_name,
            message_type="notification",
            subtype_xmlid="mail.mt_comment",
        )

    # بروزرسانی بالاترین آفر
        if record.offered_price > game.highest_offer:
            game.highest_offer = record.offered_price

        return record


