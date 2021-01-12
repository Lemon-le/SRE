import matplotlib.pyplot as plt
from matplotlib import patches

import numpy as np

""" 
https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.patches.Rectangle.html
"""

fig, ax1 = plt.subplots(1, 1, figsize=(15, 9))
plt.axis('off')
ax1.yaxis.set_major_locator(plt.NullLocator())
ax1.xaxis.set_major_formatter(plt.NullFormatter())



# 5大行第1行第1个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((0, 0), 30, 1, angle=0, color="CadetBlue"))
ax1.set_title("Singer Java Process Memory Distribute")
plt.annotate(s="JVM Total Memory Distribution",  xytext=(1, 0.3), xy=(0, 0), weight="normal")

# 5大行第2行第1个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((0, 1), 18, 1, angle=0, color="Coral"))
plt.annotate(s="Heap Memory (-Xmx)",  xytext=(1, 1.5), xy=(0, 0), weight="normal")

# 5大行第2行第2个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((18, 1), 12, 1, angle=0, color="SandyBrown"))
plt.annotate(s="None-Heap",  xytext=(19, 1.5), xy=(0, 0), weight="normal")

# 5大行第3行第1个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((0, 2), 10, 1, angle=0, color="LightSeaGreen"))
plt.annotate(s="Young Generation \n(-XX:MaxNewSize)",  xytext=(0.5, 2.3), xy=(0, 0), weight="normal")

# 5大行第3行第2个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((10, 2), 10, 1, angle=0, color="Tan"))
plt.annotate(s="Old Generation",  xytext=(11, 2.4), xy=(0, 0), weight="normal")

# 5大行第3行第3个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((20, 2), 7, 1, angle=0, color="PaleVioletRed"))
plt.annotate(s="Permannet Generation\n(-XX:PermSize)",  xytext=(21, 2.3), xy=(0, 0), weight="normal")


# 5大行第4行第1个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((0, 3), 3, 3, angle=0, color="Silver"))
plt.annotate(s="Virtual or reserved",  xytext=(1, 3.8), xy=(0, 0), weight="normal", rotation=90)


# 5大行第4行第2个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((3, 3), 7, 0.8, angle=0, color="plum"))
plt.annotate(s="-XX:NewSize",  xytext=(3.5, 3.2), xy=(0, 0), weight="normal")


# 5大行第4行第3个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((3, 3.8), 3, 2.2, angle=0, color="Wheat"))
plt.annotate(s="Eden",  xytext=(4, 4.7), xy=(0, 0), weight="normal", rotation=90)


# 5大行第4行第4个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((6, 3.8), 2, 2.2, angle=0, color="Salmon"))
plt.annotate(s="Survivor 1",  xytext=(6.8, 4.5), xy=(0, 0), weight="normal", rotation=90)


# 5大行第4行第5个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((8, 3.8), 2, 2.2, angle=0, color="MistyRose"))
plt.annotate(s="Survivor 2",  xytext=(8.8, 4.5), xy=(0, 0), weight="normal", rotation=90)


# 5大行第4行第5个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((10, 3), 7, 3, angle=0, color="RosyBrown"))
plt.annotate(s="Tenured",  xytext=(13, 4.3), xy=(0, 0), weight="normal", rotation=90)


# 5大行第4行第6个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((17, 3), 3, 3, angle=0, color="Silver"))
plt.annotate(s="Virtual or reserved",  xytext=(18, 3.8), xy=(0, 0), weight="normal", rotation=90)



# 5大行第4行第6个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((20, 3), 7, 3, angle=0, color="SandyBrown"))
plt.annotate(s="PermGen",  xytext=(22.8, 4.3), xy=(0, 0), weight="normal", rotation=90)


# 5大行第4行第7个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((27, 3), 3, 3, angle=0, color="Silver"))
plt.annotate(s="Virtual or reserved",  xytext=(28, 3.8), xy=(0, 0), weight="normal", rotation=90)

# 5大行第5行第1个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((3, 6), 14, 1, angle=0, color="CadetBlue"))
plt.annotate(s="Total: -Xms",  xytext=(8, 6.3), xy=(0, 0), weight="normal")

# 5大行第5行第2个图
ax1.axis([0, 30, 0, 8])  #坐标轴
ax1.add_patch(patches.Rectangle((20, 6), 10, 1, angle=0, color="SteelBlue"))
plt.annotate(s="Total: -XX:MaxPermSize",  xytext=(22, 6.3), xy=(0, 0), weight="normal")


plt.savefig('Java_Memory_Distribution.png')