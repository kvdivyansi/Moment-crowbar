import matplotlib.pyplot as plt
import numpy as np
import math

temp=0
while temp<=0:
    f=input("Enter the amount of force applied by the man(in N): ")
    ll=input("Enter the distance(in mm):")
    if (f.isdigit() and ll.isdigit() ):
        temp+=1
        F=float(f)
        l=float(ll)
        #print("this block is printed if")
    elif not(f.isalpha()):
        F=float(f)
        l=float(ll)
        temp+=1
        #print("this elif")
    else:
        print("ERROR-invalid entry--enter numbers ")
#print(F)
#print(l)

L=l/1000
i=0
while i==0:
    a=float(input('Enter the angle made by the crowbar and ground:'))
    if a in range(0,91):
        i=1
    else:
        i=0
        print("Enter a vaild input. It can have a value between 0 to 90. Since the crowbar cannot go underground or over the block.")

theta_bar = np.radians(a)
b=float(input('Enter the angle between the perpendicular and the forces:'))
theta_force = theta_bar + np.radians(b)+math.radians(90)

O = np.array([0, 0])
A = np.array([L * np.cos(theta_bar), L * np.sin(theta_bar)])

Fx = F * np.cos(theta_force)
Fy = F * np.sin(theta_force)

plt.plot([O[0], A[0]], [O[1], A[1]], 'k-', linewidth=4, label='Bar (OA)')
plt.quiver(A[0], A[1], Fx/200, Fy/200, angles='xy', scale_units='xy', scale=1.0, color='r', label='Force (350 N)')
plt.plot([O[0], A[0]+0.1], [0, 0], 'k--', alpha=0.4)

theta_perp = theta_bar + np.pi/2
length_perp = 0.2
x_perp = [A[0], A[0] + length_perp * np.cos(theta_perp)]
y_perp = [A[1], A[1] + length_perp * np.sin(theta_perp)]
plt.plot(x_perp, y_perp, 'b--', linewidth=2, label='Perpendicular to Bar')

plt.text(O[0]-0.02, O[1]-0.02, 'O', fontsize=12, fontweight='bold')
plt.text(A[0]+0.02, A[1], 'A', fontsize=12, fontweight='bold')
plt.text(0.25, 0.02,a, fontsize=11, color='blue')
plt.text(A[0]-0.2, A[1]+0.05,b, fontsize=11, color='blue')
plt.text(0.4,0.1,l,fontsize=11,color='blue')
plt.text(0.4,0.4,F,fontsize=11,color='blue')

f=F*math.cos(math.radians(b))
m=-(L*f)
print(f"The moment made by the force {F} about the point O is {m:.3f} Nm ",end='')
if m>0:
    print("in anticlockwise direction ")
else:
    print("in clockwise direction")

plt.title('Free Body Diagram of the Bar OA', fontsize=14)
plt.axis('equal')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.grid(True)
plt.legend()
plt.show()
