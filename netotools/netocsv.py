""" Tools for using Neto import/export wizard with csv files """

from dataclasses import dataclass


@dataclass(frozen=True)
class NetoProductFields:
    """Neto field values to use when compiling product data .csv files"""

    SKU: str = "SKU*"
    PARENTSKU: str = "Parent SKU"
    NAME: str = "Name"  # Maxlength 150
    DESCRIPTION: str = "Description"  # HTML Description
    SUBTITLE: str = "Subtitle"
    BRAND: str = "Brand"  # Max length 50
    ACTIVE: str = "Active"  # Boolean
    APPROVED: str = "Approved"  # Boolean
    APPROVEDFORNETOPOS: str = "Approved for Neto POS"  # Boolean
    VIRTUAL: str = "Virtual"  # Boolean
    RRP: str = "RRP"
    AVERAGECOSTPRICE: str = "Average Cost Price"
    PRICEDEFAULT: str = "Price (Default)"
    DEFAULTPURCHASEPRICE: str = "Default Purchase Price"
    TAXFREEITEM: str = "Tax Free Item"
    QTYINSTOCK: str = "Qty In Stock"
    CATEGORY: str = "Category Full Path List (Product Category)"
    BARCODE: str = "Barcode"
    HEIGHTSHIPPING: str = "Height (Shipping)"
    CUBICSHIPPING: str = "Cubic (Shipping)"
    WIDTHSHIPPING: str = "Width (Shipping)"
    SELLINGUNITOFMEASURE = "Selling Unit of Measure"
    SEOMETAKEYWORDS: str = "SEO Meta Keywords"
    LENGTHSHIPPING: str = "Length (Shipping)"
    WEIGHTSHIPPING: str = "Weight (shipping)"
    SHIPPINGCATEGORY: str = "Shipping Category"
    SEOMETADESCRIPTION: str = "SEO Meta Description"
    SEOPAGETITLE: str = "SEO Page Title"
    SPECIFICTYPE1: str = "Specific Type 1"
    SPECIFICVALUE1: str = "Specific Value 1"
    SPECIFICTYPE2: str = "Specific Type 2"
    SPECIFICVALUE2: str = "Specific Value 2"
    CUSTOMLABELCODE: str = "Custom Label/Code"  # Max length 50
    SPLITFORWAREHOUSEPICKING: str = "Split for Warehouse Picking"
    HANDLINGTIMEDAYS: str = "Handling Time (days)"
    OVERFLOWLOCATION2: str = "Overflow Location 2"
    KITCOMPONENTS: str = "Kit Components"
    MODEL: str = "Model #"
    EBAYSCENARIONAME: str = "Ebay Scenario Name"
    PICKZONE: str = "Pick Zone"
    JOB: str = "Job"
    SUBTYPE: str = "Subtype"
    UPSELLPRODUCTS: str = "Upsell Products"
    INTERNALNOTES: str = "Internal Notes"
    WARRANTY: str = "Warranty"
    OVERFLOWLOCATION1 = "Overflow Location 1"
    EDITABLEKIT = "Editable Kit"
    GROUP = "Group"
    REQUIRESPACKAGING = "Requires Packaging"
    TYPE = "Type"
    SORTORDER2 = "Sort Order 2"
    CARTONS = "Cartons"
    SORTORDER1 = "Sort Order 1"
    PROMOTIONPRICE = "Promotion Price"
    SUPPLIERPRODUCTNAME = "Supplier Product Name"
    EBAYTITLE = "Ebay Title"
    TAXINCLUSIVE = "Tax Inclusive"
    SPECIFICATIONS = "Specifications"
    LOCATIONINFACTORY = "LocationInFactory"
    SPECIFICTYPE3 = "Specific Type 3"
    TAXCATEGORY = "Tax Category"
    EBAYAUCTIONTITLE = "Ebay AuctionTitle"
    PROMOTIONSTARTDATE = "Promotion Start Date"
    SHORTDESCRIPTION = "Short Description"
    CONDITION = "Condition"
    PROMOTIONEXPIRYDATE = "Promotion Expiry Date"
    RESTOCKQTY = "Restock Qty"
    FORMAT = "Format"
    PREORDERQTY = "Preorder Qty"
    DATEADDED = "Date Added"
    WARRANTY = "Warranty"
    TERMSANDCONDITIONS = "Terms And Conditions"
    PRIMARYSUPPLIER = "Primary Supplier"
    SUPPLIERITEMCODE = "Supplier Item Code"
    DATEOFARRIVAL = "Date Of Arrival"
    OLDPRODUCTID = "Old Product ID"
    FEATURES = "Features"
    TRADEPRICE = "Trade Price"
    RESTRICTEDTOUSERGROUPS = "Restricted To User Group(s)"
    ARTISTAUTHOR = "Artist/Author"
    MAINIMAGEDOWNLOADURL = "Main Image Download URL"
    PROMOTIONID = "Promotion ID"
    DISPLAYTEMPLATE = "Display Template"
    PRICEWEBSITE = "Price (WEBSITE)"
    SPECIFICVALUE3 = "Specific Value 3"
    PRICEEBAYNOPOSTAGE = "Price (eBay NO Postage)"
    PRICEEBAY = "Price (eBay)"
    PRICEPOS = "Price (POS)"
    PRICEEBAYINCLSHIPPING = "Price (eBay Incl shipping)"
    PRICETRADEPRICE = "Price (Trade Price)"
    PRICEHMGJEFF = "Price (HMG Jeff)"
    PRICEINDENT = "Price (Indent)"
    PRICECOSTNORMALEX = "Price (Cost Normal Ex)"
    EPIDFOREBAYUNITEDSTATES = "ePID for eBay United States"
    EPIDFOREBAYCANADAENGLISH = "ePID for eBay Canada (English)"
    EPIDFOREBAYUK = "ePID for eBay UK"
    EPIDFOREBAYAUSTRALIA = "ePID for eBay Australia"
    EPIDFOREBAYGERMANY = "ePID for eBay Germany"
    QTYINSTOCKROADRUNNER = "Qty In Stock (roadrunner)"
    QTYINSTOCKSECONDARYWAREHOUSE = "Qty In Stock (Secondary Warehouse)"
    GENERATEURLAUTOMATICALLY = "Generate URL Automatically"  # Boolean default = True
    PRODUCTURL = "Product URL"


class NetoFieldTools(NetoProductFields):
    def price_update_fields(self) -> list:
        """Neto fields for price updates"""
        self.labels = [
            self.SKU,
            self.RRP,
            self.DEFAULTPURCHASEPRICE,
            self.PRICECOSTNORMALEX,
            self.TRADEPRICE,
            self.PRICETRADEPRICE,
            self.PRICEWEBSITE,
            self.PRICEEBAYNOPOSTAGE,
            self.PRICEEBAY,
        ]

        return self.labels

    def product_update_fields(self) -> list:
        """Neto fields for adding/updating new products"""
        return [
            self.SKU,
            self.NAME,
            self.DESCRIPTION,
            self.ACTIVE,
            self.APPROVED,
            self.APPROVEDFORNETOPOS,
            self.VIRTUAL,
            self.BRAND,
            self.DEFAULTPURCHASEPRICE,
            self.PRICECOSTNORMALEX,
            self.TAXFREEITEM,
            self.CATEGORY,
            self.HEIGHTSHIPPING,
            self.WIDTHSHIPPING,
            self.LENGTHSHIPPING,
            self.WEIGHTSHIPPING,
            self.SEOPAGETITLE,
            self.CUSTOMLABELCODE,
            self.EBAYTITLE,
            self.PRIMARYSUPPLIER,
            self.SUPPLIERITEMCODE,
            self.MAINIMAGEDOWNLOADURL,
            self.RRP,
            self.TRADEPRICE,
            self.PRICETRADEPRICE,
            self.PRICEWEBSITE,
            self.PRICEEBAYNOPOSTAGE,
            self.PRICEEBAY,
        ]

    def all_fields(self) -> list:
        members = [
            attr
            for attr in dir(self)
            if not callable(getattr(self, attr)) and not attr.startswith("__")
        ]

        return [getattr(self, member) for member in members]
