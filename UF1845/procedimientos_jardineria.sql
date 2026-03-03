use jardineria;

-- Plantilla de procedimiento almacenado

/*
drop procedure if exists <nombre>;

delimiter $$

create procedure <nombre>()
begin


end $$

delimiter ;


*/

drop procedure if exists saludo;

delimiter $$

create procedure saludo()
begin
	select "Bienvenido al maravilloso mundo del SQL.";
end $$

delimiter ;

call saludo();  

-- ---------------------------

drop procedure if exists saludo_p;

delimiter $$

create procedure saludo_p(in v_persona varchar(10))
begin
	select concat("Bienvenido al maravilloso mundo del SQL",
				  ", "
				 ,v_persona) ;
end $$

delimiter ;


call jardineria.saludo_p("Teo");

-- -------------------
-- 1. Devuelve un  listado con el código de oficina y la ciudad donde hay oficinas

drop procedure if exists oficina_ciudad;

delimiter $$

create procedure oficina_ciudad()
begin
	select o.codigo_oficina , o.ciudad 
	from oficina o ;

end $$

delimiter ;


call oficina_ciudad();

-- ------------------
drop procedure if exists oficina_ciudad_pais;

delimiter $$

create procedure oficina_ciudad_pais(v_pais varchar(50), out ok varchar(50))
begin
	select o.codigo_oficina , o.ciudad 
	from oficina o 
	where o.pais = v_pais;
	
	set ok = "Todo perfecto";

end $$

delimiter ;


call oficina_ciudad_pais('España', @resultado);

select @resultado;





