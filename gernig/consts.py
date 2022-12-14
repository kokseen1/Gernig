import os

# define all filenames here
FILENAME_BINEXP_HEADER = "binexp.h"
FILENAME_DNS_NOISE_HEADER = "dnsnoise.h"
FILENAME_DNS_ANALYSIS_HEADER = "dnsanalysis.h"
FILENAME_MAC_ANALYSIS_HEADER = 'macblacklist.h'
FILENAME_DEFINES_HEADER = "defines.h"
FILENAME_NOISY = "noisy.exe"
FILENAME_PROCESS_ANALYSIS = "processanalysis.h"

RESOLVED_DOMAINS_FILEPATH = os.path.join('dns', 'resolved-domains.txt')
FAKE_DOMAINS_FILEPATH = os.path.join('dns', 'fake-domains.txt')
WORDLIST_FILEPATH = os.path.join('dns', 'wordlist.txt')
TLD_FILEPATH = os.path.join('dns', 'tld.txt')

TEMPLATE_CHAR_ARRAY = "unsigned char BINARY_ARRAY[] = {{ {} }};"
TEMPLATE_DEFINE = "#define {}\n"

TEMPLATE_PRINT_NOISE_TEXT = '_PRINT_NOISE_TEXT "{}"'
TEMPLATE_DNS_NOISE_WORDLIST_ARG = 'static std::vector<std::string> WORDLIST = {{ {} }};\n'
TEMPLATE_DNS_NOISE_TLD_ARG = 'static std::vector<std::string> TLD = {{ {} }};\n'

PRINT_NOISE_ENABLED = "_PRINT_NOISE_ENABLED"
DNS_NOISE_ENABLED = "_DNS_NOISE_ENABLED"
FILE_NOISE_ENABLED = "_FILE_NOISE_ENABLED"
NETWORK_NOISE_ENABLED = "_NETWORK_NOISE_ENABLED"
REGISTRY_NOISE_ENABLED = "_REGISTRY_NOISE_ENABLED"
TIMESTOMPER_NOISE_ENABLED = "_TIMESTOMPER_NOISE_ENABLED"

DNS_ANALYSIS_ENABLED = "_DNS_ANALYSIS_ENABLED"
TEMPLATE_DNS_ANALYSIS_FAKE_ARG = 'std::vector<std::string> FAKE_DNS = {{ {} }};\n'
TEMPLATE_DNS_ANALYSIS_REAL_ARG = 'std::vector<std::string> REAL_DNS = {{ {} }};\n'

# for mac address checks
MAC_ANALYSIS_ENABLED = "_MAC_ANALYSIS_ENABLED"
TEMPLATE_MAC_ANALYSIS_ARG = 'std::vector<std::string> MAC_BLACKLIST = {{ {} }};\n'

CPUID_ANALYSIS_ENABLED = "_CPUID_ANALYSIS_ENABLED"

DEBUG_ANALYSIS_ENABLED = "_DEBUG_ANALYSIS_ENABLED"

PROCESS_ANALYSIS_ENABLED = "_PROCESS_ANALYSIS_ENABLED"
TEMPLATE_PROCESS_ANALYSIS_ARG = 'std::vector<std::string> PROCESS_LIST = {{ {} }};\n'

SLEEP_ANALYSIS_ENABLED = "_SLEEP_ANALYSIS_ENABLED"
TEMPLATE_SLEEP_ANALYSIS_ARG = '_SLEEP_TIME {}'

EVENTLOG_BLIND_ENABLED = "_EVENTLOG_BLIND_ENABLED"
BLOCKDLL_BLIND_ENABLED = "_BLOCKDLL_BLIND_ENABLED"
ACG_BLIND_ENABLED = "_ACG_BLIND_ENABLED"
