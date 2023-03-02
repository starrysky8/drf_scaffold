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

        os.chdir(BASE_DIR)
        try:
            os.system(f"{sys.executable} manage.py makemigrations")
            os.system(f"{sys.executable} manage.py migrate --fake-initial")
        except Exception as e:
            logger.info(f"数据库迁移失败: {e}")
            sys.exit(1)

    def exec(self):
        """开始执行"""
        pass


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="用于执行一些终端命令")
    parse.add_argument("--migrate-db", action="store_true", help="数据库迁移")

    if len(sys.argv) < 2:
        parse.print_help(sys.stderr)
        sys.exit(2)

    args = parse.parse_args()
    print(args)
    Aide(args=args).exec()
