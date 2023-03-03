import os
import sys
import json
import logging
import argparse
import django


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_scaffold.settings")
django.setup()

logging.getLogger().handlers = []
logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)
logger = logging.getLogger("aide")


class Aide(object):
    """用于执行一些终端命令"""

    def __init__(self, args) -> None:
        self.args = args

    def migrate_db(self):
        """数据库迁移"""

        logger.info(">>> 开始迁移数据库")

        os.chdir(BASE_DIR)
        try:
            os.system(f"{sys.executable} manage.py makemigrations")
            os.system(f"{sys.executable} manage.py migrate --fake-initial")
        except Exception as e:
            logger.error(f"!!! 数据库迁移失败: {e}")
            self.exit(1)

        logger.info(">>> 迁移数据库完成")

    def exit(self, code=0):
        logger.info("*** 助手程序执行结束 ***")
        sys.exit(code)

    def exec(self):
        """开始执行"""
        logger.info("*** 助手程序开始执行 ***")

        store_true_keys = ["migrate_db"]
        for k in store_true_keys:
            if getattr(self.args, k):
                # 执行具体方法
                getattr(self, k)()
        
        
        self.exit()


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="用于执行一些终端命令")
    parse.add_argument("--migrate-db", action="store_true", help="数据库迁移")

    if len(sys.argv) < 2:
        parse.print_help(sys.stderr)
        sys.exit(2)

    args = parse.parse_args()
    Aide(args=args).exec()
