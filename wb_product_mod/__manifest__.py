# -*- coding: utf-8 -*-
{
    'name': "Modificaciones Producto y Compra",

    'summary': """
        Modificaciones al template del producto para uso general e interno""",

    'description': """
        Este módulo agrega diferentes modificaciones y campos al product_template
        
        -Medidas de empaque (Largo, alto, ancho, peso)
        -Medidas de producto (Largo, alto, ancho, peso)
        -Catálogos de marketplace
        -Categoría por MP
        -Importación/Nacional
        -Esquema logístico original por canal/tienda
        -Comprador
        -Agotado de industria
        -Producto sustituto/espejo
        -Comprador
        -Costo anterior/reposición/último pagado
        -Códigos por Marketplace/Proveedor
        -Agrava IVA
        -Fechas de primera y última salida
        -Planning
        -Esquema logístico

    """,

    'author': "WonderBrands",
    'website': "http://www.wonderbrands.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'product',
                'sale',
                'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/product_supplierinfo_views.xml',
        'views/product_template_views.xml',
        'views/res_partner_views.xml',
        'views/purchase_order_views.xml',
        'views/purchase_order_line_views.xml',
        'views/stock_picking_views.xml',
        'views/sale_order_views.xml',
        'views/templates.xml',

        'data/cat.amazon.csv',
        'data/cat.claro.csv',
        'data/cat.coppel.csv',
        'data/cat.elektra.csv',
        'data/cat.elenas.csv',
        'data/cat.linio.csv',
        'data/cat.liverpool.csv',
        'data/cat.meli.csv',
        'data/cat.sears.csv',
        'data/cat.shopee.csv',
        'data/cat.vivia.csv',
        'data/cat.walmart.csv',
        'data/cat.web.csv',
        'data/esquema.logistico.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
