import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-shopinvader-odoo-shopinvader",
    description="Meta package for shopinvader-odoo-shopinvader Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-base_url',
        'odoo13-addon-shopinvader',
        'odoo13-addon-shopinvader_algolia',
        'odoo13-addon-shopinvader_assortment',
        'odoo13-addon-shopinvader_backend_image_proxy',
        'odoo13-addon-shopinvader_cart_expiry',
        'odoo13-addon-shopinvader_category_image_for_product',
        'odoo13-addon-shopinvader_customer_multi_user',
        'odoo13-addon-shopinvader_customer_multi_user_wishlist',
        'odoo13-addon-shopinvader_customer_price',
        'odoo13-addon-shopinvader_customer_price_wishlist',
        'odoo13-addon-shopinvader_delivery_carrier',
        'odoo13-addon-shopinvader_delivery_instruction',
        'odoo13-addon-shopinvader_elasticsearch',
        'odoo13-addon-shopinvader_guest_mode',
        'odoo13-addon-shopinvader_image',
        'odoo13-addon-shopinvader_import_image',
        'odoo13-addon-shopinvader_lead',
        'odoo13-addon-shopinvader_locomotive',
        'odoo13-addon-shopinvader_locomotive_algolia',
        'odoo13-addon-shopinvader_locomotive_guest_mode',
        'odoo13-addon-shopinvader_locomotive_sale_profile',
        'odoo13-addon-shopinvader_locomotive_wishlist',
        'odoo13-addon-shopinvader_notification_default',
        'odoo13-addon-shopinvader_partner_firstname',
        'odoo13-addon-shopinvader_product_media',
        'odoo13-addon-shopinvader_product_stock',
        'odoo13-addon-shopinvader_product_stock_state',
        'odoo13-addon-shopinvader_product_template_multi_link',
        'odoo13-addon-shopinvader_product_template_multi_link_date_span',
        'odoo13-addon-shopinvader_product_variant_multi_link',
        'odoo13-addon-shopinvader_product_variant_selector',
        'odoo13-addon-shopinvader_sale_packaging',
        'odoo13-addon-shopinvader_sale_packaging_wishlist',
        'odoo13-addon-shopinvader_sale_profile',
        'odoo13-addon-shopinvader_search_engine',
        'odoo13-addon-shopinvader_wishlist',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
