"""
p3_fi_transactions package

Budget Model applies mostly to transactions from financial institutions (FI). This package 
has the functionality to intake transactions from a financial institution (FI) and process them into
a budget model. The package is designed to work with Excel workbooks, specifically for budgeting.
"""

__author__ = "Paul Painter"
__version__ = "0.1.0"
__copyright__ = "2024 Paul Painter"
__name__ = "p3_excel_budget"
__description__ = "Work with Excel wookboo data for budgeting functions."
__license__ = "MIT"

from .budget_model_constants import *

from .budget_model import (
    BudgetModel,
    log_BDM_info,
    log_BSM_info,
    check_budget_model,
)

from .budget_model_template import (
    BudgetModelTemplate,
    tryout_budget_model_template)

from .budget_storage_model import (
    bsm_save,
    bsm_load,
    bsm_bm_store_abs_path,
)

from .budget_categorization import (
    execute_worklow_categorization,
    check_budget_category,
    map_budget_category,
)

from .category_mapping import (
    map_category,
    category_map_count,
)

__all__ = [
    "bsm_save",
    "bsm_load",
    "bsm_bm_store_abs_path",
    "BudgetModel",
    "log_BDM_info",
    "log_BSM_info",
    "BudgetModelTemplate",
    "tryout_budget_model_template",
    "execute_worklow_categorization"
    "check_budget_model",
    "__create_config_template__"
]

def __create_config_template__() -> BudgetModelTemplate:
    """Create a BudgetModelTemplate instance."""
    """

    Returns:
        BudgetModelTemplate: A BudgetModelTemplate instance.
    """
    # Create a BudgetModelTemplate instance.
    bmt = BudgetModelTemplate()
    return bmt