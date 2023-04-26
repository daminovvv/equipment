import re

from django.core.validators import RegexValidator


def validate_sn(sn, mask_sn):
    """Validates SN according to mask of equipment type"""
    translate = {
        "N": "([0-9])",
        "A": "([A-Z])",
        "a": "([a-z])",
        "X": "([A-Z]|[0-9])",
        "Z": "(-|_|@)",
    }
    sn_pattern = re.compile(
        r"^{}$".format("".join(translate[letter] for letter in mask_sn))
    )

    regex_validator = RegexValidator(
        regex=sn_pattern,
        message=f"Serial number does not match following mask of equipment "
        f"type: {mask_sn}, where N - number, A - uppercase letter, "
        f"a - lowercase letter, X - number or uppercase letter, "
        f"Z - symbol from the list -,_,@",
    )

    regex_validator(sn)


def process_query_params(view, soft_delete=False):
    params = {"limit": None, "offset": None}
    if soft_delete is True:
        params["deleted"] = False
    if view.action == "list":
        params.update(view.request.query_params.dict())
    del params["limit"]
    del params["offset"]
    return params
