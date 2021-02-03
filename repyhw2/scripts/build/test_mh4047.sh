#!/bin/bash
# To Run:
# $ chmod u+x test_mh4047.sh
# $ ./test_mh4047.sh
# Testing my attacks against all reference monitors

# The following r2py are problematic ones where if included in the below run will cause problems to my tests. 
# This one that hangs (?), probably deadlock: 
#	reference_monitor_am7255.r2py reference_monitor_avs395.r2py 
#	reference_monitor_kd1651.r2py reference_monitor_mmn363.r2py
#	reference_monitor_pnd218.r2py reference_monitor_rs5247.r2py 
#	reference_monitor_rwl251.r2py reference_monitor_vg975.r2py 
# This monitor has code errors e.g. untestable monitor: reference_monitor_as6926.r2py
# This monitor raises exceptions e.g. untestable monitor: reference_monitor_srk459.r2py reference_monitor_syy274.r2py


# Round 1. Break the class. 
for ref in reference_monitor_mh4047.r2py reference_monitor_aak561.r2py  reference_monitor_aj1872.r2py reference_monitor_asp550.r2py 
	do
		echo $ref 
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest1.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest2.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest3.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest4.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest5.r2py

	done

# The following are unbreakable: reference_monitor_abb469.r2py reference_monitor_as9688.r2py reference_monitor_az1148.r2py 

# Round 2.
for ref in reference_monitor_bc1475.r2py reference_monitor_ca1621.r2py reference_monitor_dj1029.r2py reference_monitor_dy648.r2py  reference_monitor_kab808.r2py 
	do
		echo $ref 
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest1.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest2.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest3.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest4.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest5.r2py

	done

# The following are unbreakable: reference_monitor_cw1753.r2py reference_monitor_hjm280.r2py reference_monitor_jas1464.r2py reference_monitor_jc7195.r2py reference_monitor_jlp576.r2py

# Round 3.
for ref in reference_monitor_kz672.r2py reference_monitor_mrc596.r2py reference_monitor_n14846342.r2py reference_monitor_pat323.r2py reference_monitor_pc1960.r2py reference_monitor_pm2510.r2py 
	do
		echo $ref 
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest1.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest2.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest3.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest4.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest5.r2py

	done

# Round 4.
for ref in reference_monitor_rra304.r2py reference_monitor_sd2917.r2py reference_monitor_yyl301.r2py reference_monitor_zhz202.r2py reference_montior_rg2953.r2py
	do
		echo $ref 
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest1.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest2.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest3.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest4.r2py
		python repy.py restrictions.default encasementlib.r2py $ref mh4047_securitytest5.r2py

	done

# The following are unbreakable: reference_monitor_rtv215.r2py reference_monitor_tb1446.r2py reference_monitor_yc2394.r2py reference_monitor_yd574.r2py 



