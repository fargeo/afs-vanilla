import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"afs_vanilla"), "afs_vanilla.urls", name="afs_vanilla"),
)
