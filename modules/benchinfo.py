#==============================================================================#

import re, subprocess
from typing import List, Tuple

def llvm_stat_clean(stat_line: str) -> Tuple[str, str, int]:
    result = [_ for _ in stat_line.strip().split(maxsplit=3)]
    return (result[1], result[3], int(result[0])) if len(result) == 4 else ('', '', -1)

def parse_stats(proc_result: str) -> List[Tuple[str, str, int]]:
    return [clean_line
            for line   in proc_result.split('\n')
            if  re.search('^ *\d+\s+\S+\s+-\s+.*$', line)
            and (clean_line := llvm_stat_clean(line)) != ('', '', -1)]

# from enum import Enum
# class Color(Enum):
#   #

BenchmarkFeatures = [
  'edgecounter_number_of_edges',
  'varcounter_number_of_named_variables',
  'varcounter_number_of_variable_uses_using_getnumuses',
  'cgscc_passmgr_maximum_cgsccpassmgr_iterations_on_one_scc',
  'instcount_number_of_add_insts',
  'instcount_number_of_alloca_insts',
  'instcount_number_of_bitcast_insts',
  'instcount_number_of_br_insts',
  'instcount_number_of_call_insts',
  'instcount_number_of_fadd_insts',
  'instcount_number_of_fcmp_insts',
  'instcount_number_of_fdiv_insts',
  'instcount_number_of_fmul_insts',
  'instcount_number_of_fptosi_insts',
  'instcount_number_of_fsub_insts',
  'instcount_number_of_getelementptr_insts',
  'instcount_number_of_icmp_insts',
  'instcount_number_of_load_insts',
  'instcount_number_of_mul_insts',
  'instcount_number_of_phi_insts',
  'instcount_number_of_ret_insts',
  'instcount_number_of_sdiv_insts',
  'instcount_number_of_sext_insts',
  'instcount_number_of_sitofp_insts',
  'instcount_number_of_srem_insts',
  'instcount_number_of_select_insts',
  'instcount_number_of_store_insts',
  'instcount_number_of_sub_insts',
  'instcount_number_of_switch_insts',
  'instcount_number_of_trunc_insts',
  'instcount_number_of_unreachable_insts',
  'instcount_number_of_zext_insts',
  'instcount_number_of_basic_blocks',
  'instcount_number_of_non_external_functions',
  'instcount_number_of_instructions_of_all_types',
  'mem2reg_number_of_alloca\'s_promoted_within_one_block',
  'mem2reg_number_of_phi_nodes_inserted',
  'mem2reg_number_of_alloca\'s_promoted',
  'mem2reg_number_of_alloca\'s_promoted_with_a_single_store',
  'instcount_number_of_ashr_insts',
  'instcount_number_of_and_insts',
  'instcount_number_of_or_insts',
  'mem2reg_number_of_dead_alloca\'s_removed',
  'instcount_number_of_lshr_insts',
  'instcount_number_of_shl_insts',
  'instcount_number_of_udiv_insts',
  'instcount_number_of_urem_insts',
  'instcount_number_of_xor_insts',
  'instcount_number_of_uitofp_insts',
  'instcount_number_of_fpext_insts',
  'instcount_number_of_fptrunc_insts',
  'instcount_number_of_extractvalue_insts',
  'instcount_number_of_fptoui_insts',
  'instcount_number_of_ptrtoint_insts',
  'instcount_number_of_inttoptr_insts',
  'instcount_number_of_extractelement_insts',
  'instcount_number_of_insertelement_insts',
  'instcount_number_of_shufflevector_insts',
  'instcount_number_of_indirectbr_insts',
]
