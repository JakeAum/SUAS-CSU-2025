Thrust = 222/4;
Air_density = 1.14;
Propeller_radius = 0;
Entrance_Velocity = 0;
Exit_Velocity = 0 : 1 : 500;
RPM = 0 : 1 : 20000;



Propeller_radius = (Thrust./(Air_density*(pi.^3)*(RPM.^2))*((120.^2)/0.5)).^0.25
plot(Propeller_radius)


%DEPRECATED FEATURES:

% Propeller_radius = sqrt((2*Thrust)/Air_density*pi*Exit_Velocity.^2)

%Exit_Velocity = (RPM*(pi*Diameter)/60)

%plot(Diameter)


