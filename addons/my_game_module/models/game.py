from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date
from datetime import datetime, timedelta
# class BaseEntity(models.Model):
#     _name = 'base.entity'
#     _description = 'Base Entity Model'
#     create_date = fields.Datetime(string='Created On', readonly=True)
#     create_uid = fields.Many2one('res.users', string='Created By', readonly=True)
#     write_date = fields.Datetime(string='Last Updated On', readonly=True)
#     write_uid = fields.Many2one('res.users', string='Last Updated By', readonly=True)
    
    
    
class MyGame(models.Model):
    _name = 'mygame.game'
    _description = 'My Game Model'
    # _inherit = 'base.entity'

    # --- Fields ---
    genderlist = [("male", "Male"), ("female", "Female"),("both","Both")]
    name = fields.Char(string='Name', required=True)
    lastname = fields.Char(string='Last Name', required=True)
    game_name = fields.Char(string='game_name', required=True)
    description = fields.Char(string='description', required=True)
    gender = fields.Selection(genderlist, string='Gender')
    release_date = fields.Date(string='Release Date', required=True)
    is_paid = fields.Boolean(string="Is Paid?")
    price = fields.Float(string="Price$")
    discount_percent = fields.Float(string="Discount (%)")
    final_price = fields.Float(string="Final Price", compute='_compute_final_price', store=True)
    # --- color Fields ---
    is_today = fields.Boolean(string="Created Today", compute='_compute_color_flags')
    is_recent = fields.Boolean(string="Created Recently", compute='_compute_color_flags')
    is_old = fields.Boolean(string="Old Record", compute='_compute_color_flags')
    
    
    #  --- game price ----
    
    is_sold = fields.Boolean(string="Is Sold?", default=False)
    highest_offer = fields.Float(string="Highest Offer", readonly=True)
    offer_ids = fields.One2many('mygame.offer', 'game_id', string="Offers")

    # compute_fields
    full_name = fields.Char(
        string='Full Name',
        compute='_compute_full_name', # نام متد محاسباتی
        store=True                    # ذخیره در دیتابیس برای جستجو
    )
    
    highest_offer = fields.Float(string="Highest Offer", compute="_compute_highest_offer", store=True)
    
    # Onchange_field
    nickname = fields.Char(string='Nickname')

# -- def for sel botten
    def action_mark_as_sold(self):
        for rec in self:
            rec.is_sold = True







    @api.constrains('discount_percent', 'price', 'is_paid')
    def _check_discount_only_if_price_set(self):
        for rec in self:
            if rec.is_paid and rec.discount_percent and not rec.price:
                raise ValidationError("برای اعمال تخفیف باید ابتدا قیمت بازی را وارد کنید.")

    @api.depends('create_date')
    def _compute_color_flags(self):
        today = fields.Date.context_today(self)
        for rec in self:
            if not rec.create_date:
                rec.is_today = rec.is_recent = rec.is_old = False
                continue

            release = rec.release_date
            diff_days = (today - release).days

            rec.is_today = diff_days == 0
            rec.is_recent = 1 <= diff_days <= 3
            rec.is_old = diff_days > 3

    @api.depends('is_paid', 'price', 'discount_percent')
    def _compute_final_price(self):
        for rec in self:
            if rec.is_paid:
                discount = (rec.price * rec.discount_percent) / 100
                rec.final_price = rec.price - discount
            else:
                rec.final_price = 0.0




    # --- Constraints ---
    _sql_constraints = [
        ('name_lastname_uniq', 'unique (name, lastname)', 'ترکیب نام و نام خانوادگی باید منحصر به فرد باشد!')
    ]

    @api.constrains('release_date')
    def _check_release_date(self):
        """ بررسی می‌کند که تاریخ انتشار در آینده نباشد """
        today = fields.Date.context_today(self)
        for record in self:
            if record.release_date and record.release_date > today:
                raise ValidationError(
                    _("تاریخ انتشار (%s) نمی‌تواند در آینده باشد (امروز: %s)!")
                    % (record.release_date, today)
                )

    @api.constrains('name')
    def _check_name_format(self):
        """ بررسی می‌کند که نام فقط شامل حروف الفبا و فاصله باشد """
        for record in self:
            if record.name and not record.name.replace(' ', '').isalpha():
                 raise ValidationError(_("نام فقط می‌تواند شامل حروف الفبا و فاصله باشد."))

    # --- Compute Methods ---
    @api.depends('name', 'lastname') 
    def _compute_full_name(self):
        """ نام کامل را با ترکیب نام و نام خانوادگی محاسبه می‌کند. """
        for record in self:
            parts = [record.name, record.lastname]
            record.full_name = ' '.join(filter(None, parts))

    # --- Onchange Methods ---
    @api.onchange('name') 
    def _onchange_name_suggest_nickname(self):
        """ بر اساس ۳ حرف اول نام، یک نام مستعار پیشنهاد می‌دهد. """
        if self.name:
            suggested_nickname = self.name[:3] if len(self.name) >= 3 else self.name
            self.nickname = suggested_nickname
        else:
            self.nickname = False 
            
            
    @api.depends('offer_ids.offered_price')
    def _compute_highest_offer(self):
        for record in self:
            if record.offer_ids:
                record.highest_offer = max(record.offer_ids.mapped('offered_price'))
            else:
                record.highest_offer = 0.0

    offer_ids = fields.One2many('mygame.offer', 'game_id', string="Offers")        
            