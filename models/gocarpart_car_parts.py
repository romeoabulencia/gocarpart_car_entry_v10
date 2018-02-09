#######################################################################
# 
# Copyright (C) 2018 GoCarPart
#
# Author: romeo abulencia <romeo.abulencia@gmail.com>
# Maintainer: romeo abulencia <romeo.abulencia@gmail.com> 
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. 
# # This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>. 
#######################################################################

from odoo import models
from odoo import fields
from odoo import api

class vehicle_identification(models.Model):
    _name="gcp.vin"
    


class car_parts(models.Model):
    _name="gcp.car.parts"
    
    
    @api.onchange('vehicle_id')
    def onchange_vehicle_id(self):
        if self.vehicle_id:
            vehicle=self.vehicle_id
            self.car_brand_id=vehicle.brand_id.id
            self.car_make_id = vehicle.make_id.id
            self.car_model_id = vehicle.model_id.id
            self.car_trim_id = vehicle.trim_id.id
            
    @api.onchange('car_part_sub_categ_id')
    def onchange_car_part_sub_categ_id(self):
        self.car_part_categ_id=self.car_part_sub_categ_id.car_part_categ_id.id

            
            
    vehicle_id=fields.Many2one('gcp.vin',string="Vehicle ID")
    car_brand_id=fields.Many2one('gcp.car.brand')
    car_make_id = fields.Many2one('gcp.car.make')
    car_model_id = fields.Many2one('gcp.car.model')
    car_trim_id = fields.Many2one('gcp.car.trim')
    car_part_sub_categ_id=fields.Many2one('gcp.car.part.sub.category',string="Part Sub-Category", required=True)
    car_part_categ_id = fields.Many2one('gcp.car.part.category')
    name=fields.Char('Part Name')
    part_number = fields.Char('Part #')
    notes=fields.Text('Notes')
    state=fields.Selection([('new','New'),('used','Used')],string="Part status",default="new")
    product_id = fields.Many2one('product.template',string="Product")
    
    def product_creation(self,vals):
        temp_vals={'name':' ',
                   'public_categ_ids':[],
                   'marketplace_seller_id':self.env.user.id,
                   'gcp_car_parts_id':vals.get('gcp_car_parts_id').id or 0,
                   'is_car_part':True,
                   'status':'draft',
                   }
        if 'name' in vals:
            temp_vals['name']=vals['name']
        cr=self.env.cr
        cr.execute('select pc.id from product_public_category pc join gcp_car_part_sub_category sc on sc.name = pc.name')
        temp = cr.fetchone()
        if temp:
            temp_vals['public_categ_ids']=[(4,temp[0])]

        product_id = self.env['product.template'].create(temp_vals)
        vals.get('gcp_car_parts_id').write({'product_id':product_id.id})
        return product_id
        
    @api.model
    def create(self, vals):
        line = super(car_parts, self).create(vals) 
        #product entry creation hook
        if line:
            vals['gcp_car_parts_id']=line
            self.product_creation(vals)
        return line   
    
class product_template(models.Model):
    _inherit="product.template"
    _inherits={'gcp.car.parts':'gcp_car_parts_id'}
    
    gcp_car_parts_id = fields.Many2one('gcp.car.parts', string="Car Parts Entry")    
    is_car_part=fields.Boolean('Is a car part')

#generates car parts entry
class car_parts_wizard(models.TransientModel):
    _name="gcp.car.parts.wizard"
    
    
    def _get_default_car_parts(self):
        #fetches all car part category and sub category then creates temporary car part data until saved
        cr=self.env.cr 
        cr.execute('select sub.id,part.id from gcp_car_part_sub_category sub join gcp_car_part_category part on part.id =car_part_categ_id')
        part_temp_ids=[]
        parts_temp_data={'vehicle_id':self.env.context.get('active_id')}
        for sub_categ_id in cr.fetchall():
            parts_temp_data['car_part_sub_categ_id']=sub_categ_id[0]
            parts_temp_data['car_part_categ_id']=sub_categ_id[1]
            part_temp_ids.append((0,0,parts_temp_data.copy()))
        return part_temp_ids
            
        
        
        
    car_parts_ids = fields.Many2many('gcp.car.parts','car_part_wizard_id','car_part_id',default=_get_default_car_parts) 