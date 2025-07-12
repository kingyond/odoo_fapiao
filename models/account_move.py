from odoo import models, fields, api, _

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    # 发票类型选项
    CN_FAPIAO_TYPE_SELECTION = [
        ('special', '专用发票'),
        ('normal', '普通发票'),
        ('none', '无需开票'),
    ]

    # 更改翻译的方式：不在字段定义时使用_()
    cn_fapiao_type = fields.Selection(
        CN_FAPIAO_TYPE_SELECTION,
        string='发票类型',
        tracking=True,
    )
    cn_fapiao_code = fields.Char(
        string='发票代码',
        tracking=True,
    )
    cn_fapiao_number = fields.Char(
        string='发票编号',
        tracking=True,
    )
    
    # 在需要翻译的方法中使用_()函数
    @api.onchange('cn_fapiao_type')
    def _onchange_cn_fapiao_type(self):
        if self.cn_fapiao_type == 'none':
            self.cn_fapiao_code = False
            self.cn_fapiao_number = False
            return {
                'warning': {
                    'title': _('提示'),
                    'message': _('已选择"无需开票"，发票代码和编号已清空')
                }
            }
