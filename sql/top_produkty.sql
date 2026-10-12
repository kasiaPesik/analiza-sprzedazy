-- 3 produkty, które zarobiły najwięcej
SELECT
    produkt,
    SUM(ilosc * cena) AS przychod
FROM sprzedaz
GROUP BY produkt
ORDER BY przychod DESC
LIMIT 3;
