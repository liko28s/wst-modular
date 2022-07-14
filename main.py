import csv
import os

from scrappers.base import BaseScrapper

# Lectura del archivo de entrada
from structures.products import FarmatodoProduct, ExitoProduct, JumboProduct, Product

configuraciones = [
    {
        "pais": "Colombia",
        "fuente": "Exito.com",
        "url": "https://www.exito.com/guaro?_q=guaro&map=ft&page=pagenum",
        "product_class": ExitoProduct,
        "search_placeholder": "guaro",
        "page_placeholder": "pagenum",
        "product_selector": "div.vtex-search-result-3-x-galleryItem",
        "product_count_selector": ".vtex-search-result-3-x-totalProducts--layout > span:nth-child(1)",
        "stop_behavior": BaseScrapper.STOP_IF_NO_PRODUCTS,
        "page_type": BaseScrapper.SSR_PAGE,
        "pagination_selector": ".min-h-small",
        "sku_selector": "div.exito-product-details-3-x-elementScroll",
        "brand_selector": "span.vtex-product-summary-2-x-productBrandName",
        "product_name_selector": "span.vtex-store-components-3-x-productBrand",
        "regular_price_selector": "div.exito-vtex-components-4-x-PricePDP",
        "discount_price_selector": "div.exito-vtex-components-4-x-list-price",
        "image_selector": "img.vtex-product-summary-2-x-image",
        "do_scroll": True,
        "browser": BaseScrapper.USE_FIREFOX,
        "show_browser": False,
        "verbose": True
    },
    {
        "pais": "Colombia",
        "fuente": "Farmatodo",
        "product_class": FarmatodoProduct,
        "url": "https://www.farmatodo.com.co/buscar?product=filemon&departamento=Todos&filtros=",
        "search_placeholder": "filemon",
        "product_selector": "div.card-ftd.mb-3",
        "stop_behavior": BaseScrapper.STOP_IF_SELECTOR_IS_DISABLED,
        "page_type": BaseScrapper.SINGLE_PAGE,
        "pagination_selector": "#group-view-load-more",
        "sku_selector": "a.product-image-link",
        "brand_selector": None,
        "product_name_selector": "div.text-left",
        "regular_price_selector": "span.text-price",
        "discount_price_selector": "span.text-offer-price",
        "image_selector": "img.image",
        "do_scroll": True,
        "browser": BaseScrapper.USE_CHROME,
        "show_browser": True,
        "verbose":True
    },
    {
        "pais": "Colombia",
        "fuente": "Tiendas Jumbo",
        "product_class": JumboProduct,
        "url": "https://www.tiendasjumbo.co/bandeja?_q=bandeja&map=ft",
        "search_placeholder": "bandeja",
        "product_selector": "div.vtex-search-result-3-x-galleryItem",
        "stop_behavior": BaseScrapper.STOP_IF_SELECTOR_IS_DISABLED,
        "page_type": BaseScrapper.SINGLE_PAGE,
        "pagination_selector": "a.vtex-button",
        "sku_selector": ".vtex-checkbox__input",
        "brand_selector": ".vtex-product-summary-2-x-productBrandName",
        "product_name_selector": ".vtex-product-summary-2-x-productBrand",
        "regular_price_selector": "section:nth-child(1) > a:nth-child(1) > article:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > div:nth-child(1)",
        "discount_price_selector": "section:nth-child(1) > a:nth-child(1) > article:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)",
        "image_selector": "img.vtex-product-summary-2-x-imageNormal",
        "do_scroll": True,
    },
]
for fuente in configuraciones:
    # Instanciar un scrapper (por fuente)
    scrapper = BaseScrapper(**fuente)
    for index, product in enumerate(scrapper.get_products("desodorante lady")):
        print(
            product.sku,
            product.brand,
            product.product_name,
            product.regular_price,
            product.discount_price,
            product.image,
        )
