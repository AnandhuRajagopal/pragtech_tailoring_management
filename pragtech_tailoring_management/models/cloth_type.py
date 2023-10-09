from odoo import models, fields, api , _

class ClothType(models.Model):
    _name = 'tailoring.cloth_type'
    _description = 'tailoring_cloth_type'
    _

    name = fields.Char(string = 'Cloth Name',required=True)
    fabric_id = fields.Many2one('tailoring.fabric',string = 'Fabric')
    measurement_ids = fields.One2many('tailoring.measurement_relative', 'cloth_id',string = 'Measurement')


