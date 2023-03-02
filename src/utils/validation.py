import re


def validate_dns_name(dns_name):
    """检查 dns 名称格式，成功返回 True"""

    # 小写字母开头，由小写祖母，数字，横杠组成
    pattern = re.compile(r"^[a-z]([-a-z0-9]*[a-z0-9])?$")
    return pattern.fullmatch(dns_name) is not None


def validate_env_name(name):
    """检查环境变量名称格式, 成功返回 True"""

    pattern = re.compile(r"[-._a-zA-Z][-._a-zA-Z0-9]*")
    return pattern.fullmatch(name) is not None