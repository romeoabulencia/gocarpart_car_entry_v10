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
{
  "name"                 :  "Vehicle Information",
  "summary"              :  "Enable vehicle listings by their VIN for their parts",
  "category"             :  "Website",
  "version"              :  "1.0",
  "sequence"             :  1,
  "author"               :  "GoCarParts",
  "description"          :  """Enable vehicle listings by their VIN for their parts""",
  "depends"              :  [
                             'odoo_marketplace',
                            ],
  "data"                 :  ['views/gocarpart_car_part_category_views.xml',
                             'views/gocarpart_trim_engine_views.xml',
                             'views/gocarpart_car_parts_views.xml',
                             'views/gocarpart_vehicle_id_views.xml',
                             'views/gcp_menus.xml',
                             'views/product_views.xml',
                            #data
                            'data/gocarpart_trim_engine_data.xml',
                            'data/gocarpart_car_part_category_data.xml',
                            'data/product_public_category_data.xml',
                            'data/gocarpart_car_brand_data.xml',
                            ],
#   "qweb"                 :  ['static/src/xml/marketplace.xml'],
#   "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
#   "pre_init_hook"        :  "pre_init_check",
}
