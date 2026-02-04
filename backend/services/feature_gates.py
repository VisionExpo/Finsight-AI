FEATURES_BY_TIER = {
    "FREE": {
        "paper_trading": True,
        "backtesting": False,
        "drift_detection": False,
        "max_symbols": 3,
    },
    "PRO": {
        "paper_trading": True,
        "backtesting": True,
        "drift_detection": True,
        "max_symbols": 10,
    },
    "QUANT": {
        "paper_trading": True,
        "backtesting": True,
        "drift_detection": True,
        "max_symbols": 50,
    },
}


def is_feature_allowed(tier: str, feature: str) -> bool:
    return FEATURES_BY_TIER.get(tier, {}).get(feature, False)
