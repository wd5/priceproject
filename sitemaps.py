#from fblog.sitemap import BlogSitemap
from django.contrib.sitemaps import FlatPageSitemap
from fprice.sitemaps import ProductCategorySitemap

class MyFlatPageSitemap(FlatPageSitemap):
    def priority(self, item):
        return 0.5

sitemaps = {
    #'blog': BlogSitemap,
    'pages': MyFlatPageSitemap,
    'productcategories': ProductCategorySitemap,
}
