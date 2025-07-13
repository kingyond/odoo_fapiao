from odoo import models, fields, api, _

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    # 添加中国发票相关字段，不修改原有定义
    cn_fapiao_type = fields.Selection([
        ('none', _('No Invoice Required')),
        ('special', _('Special VAT Invoice')),
        ('general', _('General VAT Invoice'))
    ], string=_('Invoice Type'), default='none', tracking=True)
    
    cn_fapiao_code = fields.Char(string=_('Invoice Code'), tracking=True)
    cn_fapiao_number = fields.Char(string=_('Invoice Number'), tracking=True)