import numpy as np

row = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17]
column = [5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,1477,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,1477,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,1477,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,1477,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,1474,1477,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1474,1475,1477,2960,2961,2962,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584,5418,5419,5420,5421,5422,5423,5424,5425,5426,5427,5428,5429,5430,5431,5432,5433,5578,5579,5580,5581,5582,5583,5584]
value = [12.0,11.0,9.6,8.8,8.4,7.9,14.0,13.0,12.0,12.0,12.0,10.0,10.0,12.0,16.0,20.0,15.0,14.0,13.0,12.0,11.0,11.0,9.7,1.8,1.8,1.8,1.9,1.9,1.8,1.9,2.0,2.0,1.8,1.9,1.9,1.9,1.9,1.8,1.7,1.8,1.8,1.8,1.8,1.8,1.8,1.8,0.82,0.82,0.69,0.86,0.83,0.62,0.71,0.7,0.64,0.42,0.46,0.48,0.66,1.22,0.99,0.45,0.51,0.56,0.57,0.57,0.58,0.6,0.65,0.32,0.33,0.27,0.36,0.33,0.19,0.29,0.29,0.28,0.21,0.25,0.2,0.28,0.47,0.34,0.15,0.16,0.21,0.2,0.18,0.2,0.2,0.21,5.1,4.2,5.2,3.6,9.6,11.0,2.0,7.5,9.4,4.5,1.3,1.5,2.5,15.0,30.0,18.0,5.1,5.2,4.9,6.0,4.7,4.1,3.5,2.4,35.0,40.0,40.0,35.0,37.0,35.0,31.0,26.0,30.0,27.0,11.0,14.0,17.0,20.0,23.0,24.0,14.0,15.0,18.0,19.0,18.0,20.0,21.0,24.0,40.0,44.0,45.0,39.0,47.0,46.0,33.0,34.0,39.0,32.0,13.0,16.0,19.0,34.0,54.0,42.0,19.0,20.0,23.0,25.0,23.0,24.0,25.0,26.0,19.0,8.6,6.7,8.2,4.8,5.3,8.1,14.0,4.0,4.3,16.0,12.0,7.8,4.9,5.9,16.0,32.0,24.0,20.0,20.0,19.0,19.0,20.0,20.0,45.0,42.0,73.0,65.0,66.0,62.0,61.0,58.0,66.0,60.0,62.0,65.0,67.0,61.0,58.0,56.0,53.0,40.0,1.0,5.0,15.0,29.0,54.0,74.0,97.0,71.0,74.0,69.0,66.0,63.0,62.0,65.0,66.0,65.0,61.0,23.0,21.0,5.0,23.0,23.0,30.0,37.0,32.0,26.0,29.0,39.0,42.0,45.0,43.0,40.0,49.0,44.0,38.0,32.0,33.0,24.0,17.0,3.0,7.0,12.0,26.0,32.0,52.0,59.0,59.0,61.0,63.0,65.0,67.0,67.0,72.0,79.0,80.0,80.0,79.0,82.0,82.0,79.0,69.0,61.0,65.0,65.0,66.0,68.0,67.0,66.0,67.0,4.2,3.8,4.5,4.9,3.9,4.8,1.3,1.9,2.0,1.5,1.4,1.5,3.0,3.6,2.4,1.9,1.5,1.6,2.0,1.7,1.8,2.1,2.4,2.1,2.2,2.1,2.2,2.2,2.0,2.2,2.3,2.2,2.0,2.2,2.1,2.2,2.3,2.1,1.8,1.9,2.0,2.0,2.0,2.0,2.0,2.0,5.3,348.0,351.0,312.0,301.0,18.0,349.0,201.0,138.0,96.0,183.0,154.0,133.0,113.0,46.0,318.0,323.0,312.0,320.0,316.0,311.0,331.0,10.0,299.0,23.0,356.0,307.0,312.0,39.0,239.0,242.0,116.0,281.0,218.0,135.0,101.0,116.0,355.0,299.0,317.0,315.0,300.0,319.0,27.0,151.0,274.0,1.1,2.2,1.0,1.0,3.1,1.0,1.3,0.7,1.2,0.7,1.2,0.6,1.3,0.9,1.5,1.7,3.5,4.5,4.7,3.2,3.3,4.1,2.8,0.6,0.9,0.5,0.6,0.8,0.6,0.1,1.0,0.5,1.0,0.7,0.8,0.7,1.0,1.0,0.9,1.2,2.2,1.0,1.8,1.3,0.7,0.5]

row = np.array(row)
column = np.array(column)
value = np.array(value)