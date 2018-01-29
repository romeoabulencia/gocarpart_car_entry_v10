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

class car_part_category(models.Model):
    _name='gcp.car.part.category'
    
    name=fields.Char('Part Category',required=True)
    
class car_part_sub_category(models.Model):
    _name="gcp.car.part.sub.category"
    
    car_part_categ_id=fields.Many2one('gcp.car.part.category',required=True,string="Car Part Category")
    name=fields.Char('Part Sub-Category')
    
