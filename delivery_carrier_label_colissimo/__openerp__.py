# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: David BEAL
#    Copyright 2014 Akretion
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Delivery Carrier Label Colissimo',
    'version': '0.3',
    'author': 'Akretion',
    'summary': "Direct label printing for ColiPoste Colissimo transportation",
    'maintainer': 'Akretion',
    'category': 'Warehouse',
    'depends': [
        'delivery_carrier_colipostefr',
        'delivery_carrier_deposit',
        'intrastat_base',
    ],
    'description': """
Delivery Carrier Label Colissimo
================================

Colissimo product only goods in France or in foreign countries
Delivery address is the customer address.
For deliveries in dropoff sites see 'Delivery Carrier Label So Colissimo'
module

Description
-----------

* Manage Colissimo labels direct printing for 'ColisPoste - La Poste - FR'
* Add new delivery methods and a zpl report
* Implemented labels: 9L, 9V, 7Q, 8Q

Settings
--------
Company:
~~~~~~~~~~
Some informations have to be filled on two locations :

* company form (Settings > Companies > Companies):
complete address of the company, included phone

* configuration form (Settings > Configuration > Carriers > ColiPoste) :
the default test account number is 964744


Sequences:
~~~~~~~~~~~~
Some sequences are used for France destination.
Theses sequences are generated by the ERP but you also must complete
the max value of the sequence with La Poste datas


TODO
----
return label (8R)


Contributors
------------

* David BEAL <david.beal@akretion.com>


    """,
    'website': 'http://www.akretion.com/',
    'data': [
        'data/delivery.xml',
        'data/sequence.xml',
        'report/report.xml',
        'report/cn23.xml',
        #'stock_view.xml',
    ],
    'tests': [],
    'demo': [
        'demo/stock.picking.csv',
        'demo/stock.move.csv',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
    'application': False,
}
