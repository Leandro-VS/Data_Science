-- Criando algumas variaveis basicas
select t2.seller_id, t3.idade_base,

        sum(t2.price) as receita_total,
        sum (t2.price) / count(DISTINCT t2.order_id) as avg_vl_venda,
        sum (t2.price) / 6 as avg_vl_mes,
        count( DISTINCT t2.order_id) as qtde_vendas,
        count(t2.product_id) as qtde_produto,
        count(DISTINCT t2.product_id) as qtde_produto_dst,
        sum (t2.price) / count(t2.product_id) as avg_vl_produto,
        count(t2.product_id) / count(DISTINCT t2.order_id) as avg_qtde_produto_venda

from tb_orders as t1

LEFT JOIN tb_order_items as t2
on t1.order_id = t2.order_id

LEFT JOIN (
    select 
        t2.seller_id,
        cast(max( julianday('2017-04-01') - julianday(t1.order_approved_at)) as int)  as idade_base

    from tb_orders as t1

    LEFT JOIN tb_order_items as t2
    on t1.order_id = t2.order_id

    where t1.order_approved_at < '2017-04-01'
    and t1.order_status = 'delivered'

    GROUP BY t2.seller_id
) as t3 
on t2.seller_id = t3.seller_id 

where t1.order_approved_at BETWEEN '2016-10-01' 
and '2017-04-01'
and t1.order_status = 'delivered'

GROUP BY t2.seller_id;

-- select * from tb_order_items limit 10