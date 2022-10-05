""" Tools for using Neto import/export wizard with csv files """

from datetime import datetime
from enum import Enum


class NetoProductFields(Enum):
    """Neto field values to use when compiling product data .csv files"""

    SKU: str = "SKU*"
    PARENTSKU: str = "Parent SKU"
    NAME: str = "Name"
    DESCRIPTION: str = "Description"
    SUBTITLE: str = "Subtitle"
    BRAND: str = "Brand"
    ACTIVE: bool = "Active"
    APPROVED: bool = "Approved"
    APPROVEDFORNETOPOS: bool = "Approved for Neto POS"
    VIRTUAL: bool = "Virtual"
    RRP: float = "RRP"
    AVERAGECOSTPRICE: float = "Average Cost Price"
    PRICEDEFAULT: float = "Price (Default)"
    DEFAULTPURCHASEPRICE: float = "Default Purchase Price"
    TAXFREEITEM: bool = "Tax Free Item"
    QTYINSTOCK: int = "Qty In Stock"
    CATEGORY: str = "Category Full Path List (Product Category)"
    BARCODE: str = "Barcode"
    HEIGHTSHIPPING: float = "Height (Shipping)"
    CUBICSHIPPING: float = "Cubic (Shipping)"
    WIDTHSHIPPING: float = "Width (Shipping)"
    SELLINGUNITOFMEASURE: str = "Selling Unit of Measure"
    SEOMETAKEYWORDS: str = "SEO Meta Keywords"
    LENGTHSHIPPING: int = "Length (Shipping)"
    WEIGHTSHIPPING: int = "Weight (shipping)"
    SHIPPINGCATEGORY: str = "Shipping Category"
    SEOMETADESCRIPTION: str = "SEO Meta Description"
    SEOPAGETITLE: str = "SEO Page Title"
    SPECIFICTYPE1: str = "Specific Type 1"
    SPECIFICVALUE1: str = "Specific Value 1"
    SPECIFICTYPE2: str = "Specific Type 2"
    SPECIFICVALUE2: str = "Specific Value 2"
    CUSTOMLABELCODE: str = "Custom Label/Code"
    SPLITFORWAREHOUSEPICKING: bool = "Split for Warehouse Picking"
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
    OVERFLOWLOCATION1: str = "Overflow Location 1"
    EDITABLEKIT: bool = "Editable Kit"
    GROUP: str = "Group"
    REQUIRESPACKAGING: bool = "Requires Packaging"
    TYPE: str = "Type"
    SORTORDER2: str = "Sort Order 2"
    CARTONS: str = "Cartons"
    SORTORDER1: str = "Sort Order 1"
    PROMOTIONPRICE: float = "Promotion Price"
    SUPPLIERPRODUCTNAME: str = "Supplier Product Name"
    EBAYTITLE: str = "Ebay Title"
    TAXINCLUSIVE: bool = "Tax Inclusive"
    SPECIFICATIONS: str = "Specifications"
    LOCATIONINFACTORY: str = "LocationInFactory"
    SPECIFICTYPE3: str = "Specific Type 3"
    TAXCATEGORY: str = "Tax Category"
    EBAYAUCTIONTITLE: str = "Ebay AuctionTitle"
    PROMOTIONSTARTDATE: datetime = "Promotion Start Date"
    SHORTDESCRIPTION: str = "Short Description"
    CONDITION: str = "Condition"
    PROMOTIONEXPIRYDATE: datetime = "Promotion Expiry Date"
    RESTOCKQTY: int = "Restock Qty"
    FORMAT: str = "Format"
    PREORDERQTY: int = "Preorder Qty"
    DATEADDED: datetime = "Date Added"
    WARRANTY: str = "Warranty"
    TERMSANDCONDITIONS: str = "Terms And Conditions"
    PRIMARYSUPPLIER: str = "Primary Supplier"
    SUPPLIERITEMCODE: str = "Supplier Item Code"
    DATEOFARRIVAL: datetime = "Date Of Arrival"
    OLDPRODUCTID: str = "Old Product ID"
    FEATURES: str = "Features"
    TRADEPRICE: float = "Trade Price"
    RESTRICTEDTOUSERGROUPS: str = "Restricted To User Group(s)"
    ARTISTAUTHOR: str = "Artist/Author"
    MAINIMAGEDOWNLOADURL: str = "Main Image Download URL"
    PROMOTIONID: str = "Promotion ID"
    DISPLAYTEMPLATE: str = "Display Template"
    PRICEWEBSITE: float = "Price (WEBSITE)"
    SPECIFICVALUE3: str = "Specific Value 3"
    PRICEEBAYNOPOSTAGE: float = "Price (eBay NO Postage)"
    PRICEEBAY: float = "Price (eBay)"
    PRICEPOS: float = "Price (POS)"
    PRICEEBAYINCLSHIPPING: float = "Price (eBay Incl shipping)"
    PRICETRADEPRICE: float = "Price (Trade Price)"
    PRICEHMGJEFF: float = "Price (HMG Jeff)"
    PRICEINDENT: float = "Price (Indent)"
    PRICECOSTNORMALEX: float = "Price (Cost Normal Ex)"
    EPIDFOREBAYUNITEDSTATES: str = "ePID for eBay United States"
    EPIDFOREBAYCANADAENGLISH: str = "ePID for eBay Canada (English)"
    EPIDFOREBAYUK: str = "ePID for eBay UK"
    EPIDFOREBAYAUSTRALIA: str = "ePID for eBay Australia"
    EPIDFOREBAYGERMANY: str = "ePID for eBay Germany"
    QTYINSTOCKROADRUNNER: int = "Qty In Stock (roadrunner)"
    QTYINSTOCKSECONDARYWAREHOUSE: int = "Qty In Stock (Secondary Warehouse)"
    GENERATEURLAUTOMATICALLY: bool = "Generate URL Automatically"
    PRODUCTURL: str = "Product URL"

    def get_all_fields(self) -> list:
        members = [
            attr
            for attr in dir(self)
            if not callable(getattr(self, attr)) and not attr.startswith("__")
        ]
        return [getattr(self, member) for member in members]
