from odoo import models, fields, api


class assigningDriverWizard(models.TransientModel):
    _name = 'driver.wizard'
    _description = 'driver_wizard'

    driver_id = fields.Many2one('res.users',string="Driver")
    customer_id = fields.Many2one('sale.order', String="Customer",default=lambda self: self.get_active_id())
    # location = fields.Char(string ="Location", related='customer_id.')
    date = fields.Datetime(string="Date",related='customer_id.date_order')
    

    @api.model
    def get_active_id(self):
        active_id = self.env.context.get('active_id')
        if active_id:
            return self.env['sale.order'].browse(active_id)



    def driver_wizard_action(self):
        active_id = self.env.context.get("active_id")
        re = self.env['tailoring.driver'].browse([active_id])
        if re:
            res = self.env['tailoring.driver'].create({'name':self.driver_id.name,'customer_name':self.customer_id.name,'date':self.date})
        # active_id = self.env.context.get("active_id")
        # re = self.env['tailoring.driver'].browse([active_id])
        # if re:
        #     res = self.env['tailoring.driver'].create()
    


    