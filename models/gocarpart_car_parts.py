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



class car_parts(models.Model):
    _name="gcp.car.parts"
    
    vehicle_id=fields.Many2one('gcp.vin',string="Vehicle ID")
    car_part_sub_categ_id=fields.Many2one('gcp.car.part.sub.category',string="Part Sub-Category", required=True)
    car_part_categ_id = fields.Many2one('gcp.car.part.category',related="car_part_sub_categ_id.car_part_categ_id")
    name=fields.Char('Part Name')
    notes=fields.Text('Notes')
    

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