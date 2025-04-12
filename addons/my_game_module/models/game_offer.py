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
    def create(self, vals):
        record = super().create(vals)
        game = record.game_id
        if record.offered_price > game.highest_offer:
            game.highest_offer = record.offered_price
            # ارسال ایمیل به سازنده بازی
            template = self.env.ref('my_game_module.email_template_offer_notify', raise_if_not_found=False)
            if template:
                template.send_mail(game.id, force_send=True)
        return record
