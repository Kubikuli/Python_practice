def pole():
	print("seznam (list/pole)")
	a = [1, 2, 3] # Seznam (list)
	print(a)             
	b = a.append(4) # Přidá 4 na konec
	print("a.append 4 \n a=", a, "\n b=",b)
	a.extend([5, 6]) # Přidá více prvků najednou
	print("extend [5,6]",a)
	a.insert(1, 99) # Vloží 99 na index 1
	print("insert 1, 99", a)
	a.append(2)
	print("append 2", a)
	a.remove(2) # Odstraní první výskyt hodnoty 2
	print("remove 2", a)
	x = a.pop() # Odstraní a vrátí poslední prvek
	print("x =a.pop;\n a=", a,"\n x=", x)
	a.sort() # Seřadí vzestupně
	print("sort", a)
	a.sort(reverse=True)  # Seřadí sestupně
	print("sort reverse", a)
	print("Slicing a[1:6:3] =", a[1:6:3]) # Slicing sekvence[start:stop:step]
	sorted(a)
	print("sorted(a)", sorted(a)) # Seřadí vzestupně, ale nevytvoří nový seznam

def n_tice():
	print("\n\n\n ---n-tice (tuple) - neměnný seznam---")
	t = (1, 2, 3, 4, 10, 6, 7, 8, 1) # N-tice (tuple)
	print(t)
	print("t[0]", t[0]) # Přístup k prvku
	print("t[1:7:2] =", t[1:7:2]) # Slicing sekvence[start:stop:step]
	# t[0] = 99 # Chyba, n-tice jsou neměnné

def Set():
	print("\n\n\n ---Set - množina---")
	print("bez duplicit\n")

	s = { 2, 3}
	print(s)             # Množina (set)
	s.add(4)               # Přidá prvek
	print("add 4", s)
	s.update([5, 6, 1])       # Přidá více prvků
	print("update [5, 6, 1]", s)
	s.remove(2)            # Odstraní prvek (chyba pokud neexistuje)
	print("remove 2", s)
	s.discard(10)          # Odstraní prvek (bez chyby pokud neexistuje)
	print("discard 10", s)
	x = s.pop()            # Odebere a vrátí náhodný prvek
	print("x = s.pop \n s = ", s,"\n x=", x)

	s2 = {'a', 'b', '1', '2', 'c', '3'}
	print("\n s2=", s2)
	print("s2.pop()", s2.pop()) # Odebere a vrátí náhodný prvek
	# Operace množin:
	print("\nOperace množin")
	a = {1, 2, 3}
	b = {3, 4, 5}
	print("a=", a)
	print("b=", b)
	print("sjednoceni ", a | b)      # sjednocení
	print("průnik ",a & b)      # průnik
	print("rozdíl ",a - b)      # rozdíl
	print("symetrický rozdíl ",a ^ b)      # symetrický rozdíl

def dictionary():
	print("\n\n\n ---dictionary - slovník---")
	print("seznam klíč-hodnota\n")
	d = { "jmeno": "Petr", "vek": 20, "pohlavi": "M" , "auto": "lambo", "jmeno_pritele": "Max"} # Slovník (dictionary)
	print(d)             # Výpis celého slovníku
	print("d.items()", d.items()) # Výpis klíč-hodnota
	print("d['jmeno']", d["jmeno"]) # Přístup k hodnotě podle klíče
	print("d.get('vek')", d.get("vek")) # Přístup k hodnotě podle klíče
	print("d.keys()", d.keys()) # Výpis klíčů
	print("d.values()", d.values()) # Výpis hodnot
	print("d.pop('vek')", d.pop("vek")) # Odstraní a vrátí hodnotu podle klíče
	print("d", d) # Výpis celého slovníku
	d["iq"] = 100 # Přidá nový klíč-hodnota
	print("po pridani iq", d) # Výpis celého slovníku
	d["jmeno"] = "Jan" # Změní hodnotu podle klíče
	print("d['jmeno'] = 'Jan'", d) # Výpis celého slovníku
	print("d.popitem()", d.popitem()) # Odstraní a vrátí poslední přidaný klíč-hodnota
	print("d", d) # Výpis celého slovníku

	for k, v in d.items(): # Iterace přes dvojice
		print(k, v)

	print("d.clear()", d.clear()) # Odstraní všechny položky
	print("d", d) # Výpis celého slovníku
	
def main ():
	pole()
	n_tice()
	Set()
	dictionary()

if __name__ == "__main__":
	main()