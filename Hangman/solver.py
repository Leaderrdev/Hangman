import collections

# compara doua litere fara a tine cont de majuscule
def aceeasi_litera(l1, l2):
    return l1.lower() == l2.lower()


# citeste jocurile din fisier
def citeste_jocuri(nume_fisier):
    jocuri = []
    linii_invalide = []

    try:
        with open(nume_fisier, "r", encoding="utf-8") as f:
            for nr_linie, linie in enumerate(f, start=1):
                bucati = linie.strip().split(",")

                if len(bucati) != 3:
                    linii_invalide.append((nr_linie, linie.strip(), "numar gresit de campuri"))
                    continue

                id_joc, pattern_init, cuvant_corect = [b.strip() for b in bucati]

                if len(pattern_init) != len(cuvant_corect):
                    linii_invalide.append((nr_linie, linie.strip(), "lungimi diferite"))
                    continue

                jocuri.append({
                    "id": id_joc,
                    "pattern": pattern_init,
                    "cuvant": cuvant_corect
                })

        return jocuri, linii_invalide

    except FileNotFoundError:
        print(f"Fisierul '{nume_fisier}' nu a fost gasit.")
        return [], []


# filtreaza cuvintele posibile
def filtreaza_cuvinte(lista_cuvinte, pattern, litere_bune, litere_gresite):
    rezultat = []

    for cuv in lista_cuvinte:
        ok = True

        for i, ch in enumerate(pattern):
            if ch != '*' and cuv[i].lower() != ch.lower():
                ok = False
                break
            if ch == '*' and cuv[i].lower() in litere_bune:
                ok = False
                break

        if ok and all(g not in cuv.lower() for g in litere_gresite):
            rezultat.append(cuv)

    return rezultat


# rezolva un singur joc
def rezolva_joc(pattern_init, cuvant_tinta, dictionar):
    pattern = list(pattern_init)
    litere_bune = set(ch.lower() for ch in pattern if ch != '*')
    litere_gresite = set()
    incercari = 0
    incercari_facute = []

    posibile = [w for w in dictionar if len(w) == len(pattern)]

    while '*' in pattern:
        posibile = filtreaza_cuvinte(posibile, pattern, litere_bune, litere_gresite)
        if not posibile:
            break

        counter = collections.Counter()

        for w in posibile:
            for i, ch in enumerate(w):
                if pattern[i] == '*':
                    counter[ch.lower()] += 1

        if not counter:
            break

        litera = counter.most_common(1)[0][0]
        incercari += 1
        incercari_facute.append(litera)

        gasit = False
        for i, ch in enumerate(cuvant_tinta):
            if aceeasi_litera(litera, ch):
                pattern[i] = ch
                gasit = True

        if gasit:
            litere_bune.add(litera)
        else:
            litere_gresite.add(litera)

    cuvant_final = ''.join(pattern)
    status = "OK" if cuvant_final.lower() == cuvant_tinta.lower() else "FAIL"

    return {
        "incercari": incercari,
        "cuvant_final": cuvant_final,
        "status": status,
        "litere": ' '.join(incercari_facute)
    }


def main():
    fisier_intrare = "jocuri.txt"
    fisier_iesire = "rezultate.txt"

    jocuri, invalide = citeste_jocuri(fisier_intrare)

    if invalide:
        print("Linii invalide:")
        for nr, linie, motiv in invalide:
            print(f"Linia {nr}: {linie} -> {motiv}")

    toate_cuvintele = [j["cuvant"] for j in jocuri]
    rezultate = []
    total_incercari = 0

    for joc in jocuri:
        r = rezolva_joc(joc["pattern"], joc["cuvant"], toate_cuvintele)
        rezultate.append(
            f"{joc['id']},{r['incercari']},{r['cuvant_final']},{r['status']},{r['litere']}"
        )
        total_incercari += r["incercari"]

    with open(fisier_iesire, "w", encoding="utf-8") as f:
        f.write("id,incercari,cuvant_final,status,litere\n")
        for linie in rezultate:
            f.write(linie + "\n")

    print(f"Rezultate salvate in '{fisier_iesire}'")
    print(f"Total incercari: {total_incercari}")


if __name__ == "__main__":
    main()
