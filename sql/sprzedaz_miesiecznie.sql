-- Przychód w każdym miesiącu
SELECT
    strftime('%Y-%m', data)  AS miesiac,
    SUM(ilosc * cena)        AS przychod
FROM sprzedaz
GROUP BY miesiac
ORDER BY miesiac;
