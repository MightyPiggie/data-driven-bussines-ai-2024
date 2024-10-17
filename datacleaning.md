We hebben alle `nvt` en `?` kollomen verwijderd. Dit hebben we gedaan omdat er tegen ons gezegd is dat deze niet interresand zijn.

Vervolgens hebben we nog een aantal kolomen ook nog verwijderd, die worden hieronder verder toegeligt:
`stm_pplg_van` en `stm_pplg_naar`. Wij hebben hier niks aan. Er worden namelijk zowel getallen als strings door elkaar gebruikt. Dit is niet handig voor zo goed als elke model. Daarom hebben we deze kolomen verwijderd.

Ook hebben wij de kolommen `stm_equipm_omschr_gst`, `stm_equipm_omschr_mld`, `stm_sap_meldtekst`, `stm_sap_meldtekst_lang`, `stm_oorz_tkst`, `stm_oorz_tekst_kort`, `stm_schade_verhaalb_jn` verwijderd. Dit komt omdat deze beschrijvingen zijn en dus niet bruikbaar zijn voor een model.

Daarnaast hebben we ook nog de volgende kolommen verwijderd: `stm_equipm_nr_gst`,  `stm_equipm_soort_gst`, `#stm_sap_meldnr`, `stm_equipm_nr_mld`, `stm_equipm_soort_mld`. Dit komt omdat deze kolommen niet relevant zijn voor ons model omdat ze geen informatie toevoegen.

Als laatste hebben we nog de kolommen `stm_vl_post` verwijderd omdat hier veel values missen en de informatie al hebben in andere kolommen.

Wij hebben de kolomen  `stm_fh_tijd`, `stm_fh_dd` ook verwijderd omdat je hiermee anders de target variabele kan voorspellen doormiddel van begin tijd - funtie herstel tijd = duur. Dit is niet de bedoeling.

Wij hebben als feuture variabelen de volgende gekozen: `stm_geo_mld`, `stm_prioriteit`

Over de volgende feuture variabelen twijfelen we nog of ze nuttig zijn: `stm_mon_nr`, `stm_sap_meld_ddt`, `stm_km_van_mld`, `stm_km_tot_mld`

Onze target variabele is `stm_fh_duur`