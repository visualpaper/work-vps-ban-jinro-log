import os
import logging

from logging.handlers import RotatingFileHandler

from .config import get_config


config = get_config()
logger = logging.getLogger(__name__)

# application log
# - ローテート実施サイズ: 100 * 1024
# - 保持ファイル数: 7
# - 出力対象レベル: WARN 以上
app_log_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s:%(name)s - %(message)s'
)
app_log_handler = RotatingFileHandler(
    os.path.join(config.logging_path, 'app.log'),
    maxBytes=100 * 1024,
    backupCount=7,
    encoding='utf-8',
)
app_log_handler.setLevel(logging.WARN)
app_log_handler.setFormatter(app_log_formatter)


# debug log
# - ローテート実施サイズ: 100 * 1024
# - 保持ファイル数: 7
# - 出力対象レベル: INFO 以上
debug_log_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s:%(name)s - %(message)s'
)
debug_log_handler = RotatingFileHandler(
    os.path.join(config.logging_path, 'dump.log'),
    maxBytes=100 * 1024,
    backupCount=7,
    encoding='utf-8',
)
debug_log_handler.setLevel(logging.INFO)
debug_log_handler.setFormatter(debug_log_formatter)


# console log
console_log_handler = logging.StreamHandler()
console_log_handler.setLevel(logging.INFO)

# logger 出力対象は Debug 以上とする。
# ※ デフォルトでは WARN 以上のため dump/console log 用に Debug 以上としている。
logger.setLevel(logging.DEBUG)

# Uvicon Access ログを表示しないようにする。
uvicorn_access = logging.getLogger("uvicorn.access")
uvicorn_access.disabled = True

# 各 handler を登録する。
logger.addHandler(app_log_handler)
logger.addHandler(debug_log_handler)
logger.addHandler(console_log_handler)


def get_logger():
    return logger
