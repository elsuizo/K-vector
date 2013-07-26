clear all 
close all
%Scrip de prueba

%Entradas del algoritmo:
%   1)  y=f(x)
%   2)  [x_mi:x_max]
%   3)  n (numero de puntos a discretizar la funcion)

%Salida:
%   1)  N_roots (Numero de raices)
%   2)  X_e (?)


%Entradas (asi se puede separar mejor para luego hacer una funcion)
%*************************************************************************
%Preprocessing
%*************************************************************************

x_min=-5;
x_max=5;
n=10000; %Numero de muestras
y=zeros(n,1);
k_indice=1:n;% Vector de indices de x
K_vector=zeros(n,1);
x = x_min+((x_max-x_min)*(k_indice-1)/(n-1));   

y= sinc(x);
%y=-x.^2-4*x+4;

[s,I] = sort(y);

K_vector(1)=0;
K_vector(n)=n;

%Hacemos el k-vector para s
%*************************************************************************

y_min = s(1);
y_max = s(end); 

%Luego armamos la ecuacion de la recta z(x)=mx+q

n = length(y);

delta_eps = (n-1)*eps ;
m = (y_max-y_min+2*delta_eps)/(n-1);

q = y_min - m - delta_eps;

z = @(x)(m*x+q);
i=1:n;
z_i=z(i)';


for aux=2:length(y)-1
vec_aux=s<z_i(aux);
K_vector(aux)=sum(vec_aux);
end

%*************************************************************************

%Calculamos el delta
%*************************************************************************
delta=1/2*max(abs(y(2:n)-y(1:n-1)));
%*************************************************************************

%FIN Preprocesamiento




%Ahora vamos a calcular una busqueda para un y conocido(y=0) 
%*************************************************************************

y_conocido  = 0;

y_a=y_conocido-delta;

y_b=y_conocido+delta;




j_b=floor((y_a-q)/m);

j_t=ceil((y_b-q)/m);


k_start=K_vector(j_b)+1;

k_end=K_vector(j_t);

%Finalmente los elementos buscados y(i) \in [y_a;y_b] son los elementos y(I(k_busqueda))
%donde k_busqueda=k_start:k_end



k_busqueda=k_start:k_end;

y_busqueda=y(I(k_busqueda));
%Ahora si la cantidad de elementos de la base de datos es grande en promedio la
%cantidad de elementos que estan fuera del rango E0 =1 entonces esta en algunos
%de los dos extremos

if y_busqueda(1)<y_a
	y_busqueda(1)=[];%Removemos el elemento
end
if y_busqueda(end)>y_b
	y_busqueda(end)=[];%Removemos el elemento
end
y_busqueda;

X=x(I(k_busqueda));

Y=y(I(k_busqueda));

Roots=unique(round(X));
for indice=1:length(Roots)
    
    
    printf('Raiz:%d ---> %d\n',indice,Roots(indice));

end

%***********************************************************************

[X_s,J]=sort(X);

l=length(X_s);










