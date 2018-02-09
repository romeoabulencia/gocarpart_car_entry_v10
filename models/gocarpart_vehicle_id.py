# -*- coding: utf-8 -*-
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
from datetime import date, datetime


drive_selection = [('lhd_rwd', 'LHD RWD'), 
         ('rhd_rwd', 'RHD RWD'), 
         ('lhd_fwd', 'LHD FWD'), 
         ('rhd_fwd', 'RHD FWD'), 
         ('lhd_4wd', 'LHD 4WD'), 
         ('rhd_4wd', 'RHD 4WD')]
code_date_of_manufacture_selection=[('em', 'EM'), 
                                     ('ep', 'EP'), 
                                     ('eb', 'EB'), 
                                     ('er', 'ER'), 
                                     ('ea', 'EA'), 
                                     ('eg', 'EG'), 
                                     ('fc', 'FC'), 
                                     ('fk', 'FK'), 
                                     ('fd', 'FD'), 
                                     ('fe', 'FE'), 
                                     ('fl', 'FL'), 
                                     ('fy', 'FY'), 
                                     ('fs', 'FS'), 
                                     ('ft', 'FT'), 
                                     ('fj', 'FJ'), 
                                     ('fu', 'FU'), 
                                     ('fm', 'FM'), 
                                     ('fp', 'FP'), 
                                     ('gb', 'GB'), 
                                     ('gr', 'GR'), 
                                     ('ga', 'GA'), 
                                     ('gg', 'GG'),
                                      ('gc', 'GC'), 
                                      ('gk', 'GK'), 
                                      ('gd', 'GD')]
air_conditioning_selection=[('', 'N / A'),
                            ('dual_ac', 'Dual Zone Auto Temp Control A/C'),
                            ('manual_ac', 'Manual Air Conditioning'),
                                ]


class car_brand(models.Model):
    _name="gcp.car.brand"
    name=fields.Char(string="Car Brand/Manufacture")

class car_make(models.Model):
    _name="gcp.car.make"
    name=fields.Char(string="Car Make")
    car_brand_id = fields.Many2one('gcp.car.brand',string="Car Brand/Manufacturer",required=True)
    
class car_model(models.Model):
    _name="gcp.car.model"
    name=fields.Char(string="Car Model")
    car_brand_id = fields.Many2one('gcp.car.brand',string="Car Brand/Manufacturer",required=True)
    car_make_id = fields.Many2one('gcp.car.make',string="Car Make",required=True)
    
class car_trim(models.Model):
    _name="gcp.car.trim"
    name=fields.Char(string="Car Trim")
    car_brand_id = fields.Many2one('gcp.car.brand',string="Car Brand/Manufacturer",required=True)
    car_make_id = fields.Many2one('gcp.car.make',string="Car Make",required=True) 
    car_model_id=fields.Many2one('gcp.car.model',string="Car Model",required=True)   
    
class car_style(models.Model):
    _name="gcp.car.style"
    name=fields.Char(string="Car Style")

class vehicle_identification(models.Model):
    _inherit="gcp.vin"
    

    def _default_get_month(self):
        return fields.Date.from_string(fields.Date.context_today(self)).strftime('%m')

    def _default_get_year(self):
        return fields.Date.from_string(fields.Date.context_today(self)).strftime('%Y')
    
    def _get_default_seller(self):
        if self.env.user.seller:
            return True
        
    
    name=fields.Char(string='VIN', required=True)
#     production_month = fields.Selection([('01', 'January'), ('02', 'February'), ('03', 'March'),
#                                ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'),
#                                ('08', 'August'), ('09', 'September'), ('10', 'October'),
#                                ('11', 'November'), ('12', 'December')], string='Production Month', required=True, default=_default_get_month)
    brand_id = fields.Many2one('gcp.car.brand',string="Car Brand")
    make_id = fields.Many2one('gcp.car.make', string="Car Make")
    model_id = fields.Many2one('gcp.car.model',string="Car Model")
    trim_id = fields.Many2one('gcp.car.trim',string="Car Trim")
    production_year = fields.Char('Production Year', size=4, required=False, default=_default_get_year)    
    drive =  fields.Selection(drive_selection,string="Drive")
    code_date_of_manufacture = fields.Selection(code_date_of_manufacture_selection,string="Code date of manufacture") 
    final_drive_ratio = fields.Float(string="Final Drive Ratio")
    vehicle_line=fields.Char('Vehicle Line')
    air_conditioning=fields.Selection(air_conditioning_selection,"Air Conditioning")
    body_style=fields.Char('Body Style')
    positive_territories=fields.Char('Positive Teritories')
    version=fields.Char('Version')
    exterior_paint=fields.Char('Exterior Paint')
    engine_type=fields.Char("Engine Type")
    interior_environment=fields.Char('Interior Environment')
    transmission=fields.Char('Transmission')
    interior_fabric=fields.Char('Interior Fabric')
    seller_id = fields.Many2one('res.partner',string="Shop Owner", default=_get_default_seller)
    is_seller= fields.Boolean('Is seller',store=False,default=lambda self: self.env.user.seller)
    trim_engine_id = fields.Many2one('gcp.trim.engine',string="Trim / Engine", required=True)
    car_parts_ids = fields.One2many('gcp.car.parts','vehicle_id',string="Car parts")