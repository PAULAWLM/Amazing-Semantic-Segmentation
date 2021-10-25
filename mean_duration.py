## REMOVE first line of duration.text ##


# calculation of the average runtime

import statistics

with open('/app/shared/Amazing-Semantic-Segmentation/duration.txt','r') as duration: 

    times = []
    for line in duration:
	    times.append(line.rstrip('s\n'))
    
    times_float = [float(i) for i in times]

    mean = statistics.mean(times_float)
    print('Durchschnittliche Laufzeit: {:5.6f}s'.format(mean))