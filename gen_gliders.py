import golly as g
import heapq

global ini_rect
global gliders_in

gld = g.parse("3o$2bo$bo!")
gld_pairs = zip(gld[::2], gld[1::2])

shoot_defs = []

l_edge1 = g.parse("38b2o$38b2o5b2o$45b2o3$18bo5b2o17b2o$16b3o6bo17b2o$15bo9bobo21b2o$15b2o9b2o21b2o$2o$bo$bob2o$2bo2bo$3b2o$18b2o$18b2o4$27bo3b2o$26bobo3bo20bo$25bobo3bo19b3o$21b2obobo3bo19bo$21b2obo2b4obo17b2o$25bobo3bobo$21b2ob2o2bo2bobo$22bobo2b2o3bo$10b2o10bobo$10b2o11bo5$30b2o$30b2o9$45b2o$45b2o!", -92, -2)
l_gld1 = g.parse("obo$b2o$bo!", -631, -541)

l_edge2 = g.parse("38b2o$38b2o5b2o$45b2o3$18bo5b2o17b2o$16b3o6bo17b2o$15bo9bobo21b2o$15b2o9b2o21b2o$2o$bo$bob2o$2bo2bo$3b2o$18b2o$18b2o4$27bo3b2o$26bobo3bo$25bobo3bo$21b2obobo3bo$21b2obo2b4obo$25bobo3bobo$21b2ob2o2bo2bobo$22bobo2b2o3bo$10b2o10bobo$10b2o11bo2$56b2o$56bo$54bobo$54b2o$30b2o$30b2o6$32b2o$33bo$30b3o$30bo$31b2o$32bo$32bobo$33b2o5$31b2o$32bo$19b2o11bobo$20bo12b2o$20bobo$21b2o2b2o$25b2o4$20b2o4b2o$20b2o4b2o7$21b2o$20bobo$20bo$19b2o!", -89, -36)
l_gld2 = g.parse("obo$b2o$bo!", -601, -548)

l_edge3 = g.parse("42bo$42b3o$38bo6bo$37bobo4b2o$37bobo$35b3ob2o20bo$34bo24b3o$28bo6b3ob2o17bo$28b3o6bob2o17b2o$31bo$18bo11b2o$16b3o36b2o$15bo38bo2bo$15b2o38b2o$2o$bo$bob2o$2bo2bo$3b2o$18b2o$18b2o23b2o$43bo$44b3o$46bo$27bo3b2o$26bobo3bo$25bobo3bo$21b2obobo3bo$21b2obo2b4obo$25bobo3bobo$21b2ob2o2bo2bobo$22bobo2b2o3bo$10b2o10bobo$10b2o11bo3b2o$27bobo$28bo58$125b2o$125bo$126b3o$128bo!", -122, 45)
l_gld3 = g.parse("2bo$obo$b2o!", -634, -462)

l_edge4 = g.parse("67b2o$67bobo$69bo$63b2o3bob2o$64bo3bo3bo$52b2o10bob2ob2obo$27b2o24bo11bobobobo$28bo13b2o6b3o$28bobo11b2o6bo$18bo10b2o$16b3o$15bo$15b2o$2o$bo$bob2o$2bo2bo$3b2o$18b2o$18b2o$56b2o$56b2o2$27bo3b2o$26bobo3bo5b2o3b2o$25bobo3bo7bo3bo$21b2obobo3bo5b3o5b3o$21b2obo2b4obo3bo9bo$25bobo3bobo$21b2ob2o2bo2bobo$22bobo2b2o3bo$10b2o10bobo$10b2o11bo!", -123, 40)
l_gld4 = g.parse("o$b2o$2o!", -630, -464)

clock_insert = g.parse("151bob2o$151b2obo2$149b5o$149bo4bo2b2o$152bo2bo2bo$152b2obobo$149bo5bob2o$148bobo4bo$148bo2bo2b2o$149b2o9$141b2o$141b2o8$127b2o22b2o$126bo2bo21bo$127b2o23b3o$154bo6$144b2o$144bo$145b3o$147bo7$197bob2o$197b2obo2$195b5o$195bo4bo2b2o$198bo2bo2bo$198b2obobo$195bo5bob2o$73bo120bobo4bo$73b3o118bo2bo2b2o$69bo6bo118b2o$68bobo4b2o$68bobo$66b3ob2o20bo$65bo24b3o$59bo6b3ob2o17bo$59b3o6bob2o17b2o$62bo$49bo11b2o$47b3o36b2o99b2o$46bo38bo2bo98b2o$46b2o38b2o$31b2o$32bo$32bob2o$33bo2bo$34b2o$49b2o$49b2o23b2o97b2o22b2o$74bo97bo2bo21bo$75b3o95b2o23b3o45bob2o$77bo122bo45b2obo$58bo3b2o$57bobo3bo180b5o$56bobo3bo181bo4bo2b2o$52b2obobo3bo185bo2bo2bo$52b2obo2b4obo74bo108b2obobo$56bobo3bobo73b3o49b2o52bo5bob2o$52b2ob2o2bo2bobo69bo6bo48bo52bobo4bo$53bobo2b2o3bo69bobo4b2o49b3o49bo2bo2b2o$41b2o10bobo77bobo57bo50b2o$41b2o11bo76b3ob2o20bo$130bo24b3o$36bo87bo6b3ob2o17bo$34b3o87b3o6bob2o17b2o$20bo12bo93bo$9b2o7b3o12b2o79bo11b2o$10bo6bo94b3o36b2o$10bobo4b2o34bo57bo38bo2bo$11b2o38b3o57b2o38b2o83b2o$50bo45b2o138b2o$37b2o11b2o11bo33bo$37b2o24b3o31bob2o$66bo31bo2bo$65b2o32b2o$80b2o32b2o$80bo33b2o23b2o$77b2obo58bo56bo$76bo2bo60b3o53b3o23b2o22b2o$77b2o63bo49bo6bo21bo2bo21bo$62b2o59bo3b2o62bobo4b2o22b2o23b3o$26b2o34b2o58bobo3bo62bobo55bo$26bobo92bobo3bo61b3ob2o20bo$28bo88b2obobo3bo61bo24b3o$2b2o24b2o87b2obo2b4obo53bo6b3ob2o17bo$3bo45b2o3bo66bobo3bobo52b3o6bob2o17b2o$3o46bo3bobo61b2ob2o2bo2bobo55bo$o9b2o24b2o12bo3bobo61bobo2b2o3bo43bo11b2o53b2o$9bobo23bobo13bo3bobob2o45b2o10bobo49b3o36b2o28bo$9bo25bo13bob4o2bob2o45b2o11bo49bo38bo2bo28b3o$8b2o24b2o12bobo3bobo112b2o38b2o31bo$48bobo2bo2b2ob2o36b2o4bo50b2o$49bo3b2o2bobo28b2o7bobo2bobo50bo$57bobo10b2o17bo9b4o2bo49bob2o$58bo11b2o17bobo6bo4bobo50bo2bo$90b2o6b2o2b2ob2o50b2o$108bo63b2o$73b2o27b2ob4o2bo60b2o23b2o$73b2o27b2obo3b3o85bo$108bo89b3o$108b2o90bo$181bo3b2o$180bobo3bo$179bobo3bo$123bo51b2obobo3bo$123b3o49b2obo2b4obo$126bo52bobo3bobo$125b2o48b2ob2o2bo2bobo$140b2o34bobo2b2o3bo$140bo23b2o10bobo$137b2obo23b2o11bo$136bo2bo$63b2o72b2o$63b2o57b2o$122b2o2$96b2o$84b2o9bobo4b2o$84bobo8bo6bo6b2o3bo$86bo7b2o7b3o3bo3bobo$86b2o17bo4bo3bobo$111bo3bobob2o$109bob4o2bob2o$108bobo3bobo$108bobo2bo2b2ob2o$109bo3b2o2bobo$117bobo10b2o$118bo11b2o8$113b2o$113b2o$134bo$132b3o$131bo$131b2o165b2o$290b2o5bobo$151bo138bobo4bo$149b3o140bo2b2ob4o$148bo142b2obobobo2bo$135b2o11b2o11bo130bobobobo$135b2o24b3o128bobob2o$164bo128bo$163b2o$178b2o126b2o$103b2o73bo118b2o7bo$103b2o70b2obo118b2o5bobo$174bo2bo126b2o$175b2o$160b2o$124b2o34b2o$124bobo$126bo$126b2o$147b2o3bo141b2o18b2o$147bo3bobo141bo18bo$134b2o12bo3bobo137b3o21bo$133bobo13bo3bobob2o133bo2b3o14b5o$133bo13bob4o2bob2o135bo2bo13bo$132b2o12bobo3bobo138b2o2bobo12b3o$146bobo2bo2b2ob2o139b2o15bo$147bo3b2o2bobo154b4o$155bobo10b2o137b2o3bo3b2o$156bo11b2o137b2o4b3o2bo$315bob2o$292bo22bo$152bo18bo118b3o21b2o$152b3o6b2o6b3o117bo$155bo5b2o5bo120b2o$154b2o12b2o136b2o$306bo$307b3o$167b2o52bo87bo$162b2o3b2o50b3o$162b2o54bo$218b2o59b2o$278bobo5b2o$195bo42bo39bo7b2o$173bo7bo13b3o38b3o38b2o$171b3o5b3o16bo36bo$170bo7bo18b2o23b2o11b2o11bo42bo$170b2o6b2o42b2o24b3o36b2obobo$251bo34bobobobo$250b2o31bo2bobobob2o$265b2o16b4ob2o2bo$265bo21bo4bobo$262b2obo19bobo5b2o$261bo2bo20b2o$188b2o72b2o$188b2o57b2o$211b2o34b2o$211bobo$213bo$201b2o10b2o$201bo32b2o3bo$191b2o9b3o29bo3bobo$192bo11bo16b2o12bo3bobo$191bo28bobo13bo3bobob2o$191b2o27bo13bob4o2bob2o$219b2o12bobo3bobo$233bobo2bo2b2ob2o$234bo3b2o2bobo$242bobo10b2o$243bo11b2o380$436b2o11bo$436b2o10bobo$448bobo2b2o3bo$447b2ob2o2bo2bobo$451bobo3bobo12b2o$447b2obo2b4obo13bo27b2o$447b2obobo3bo13bobo28bo$451bobo3bo12b2o16bo11bo$452bobo3bo29b3o9b2o$453bo3b2o32bo$478b2o10b2o$479bo$479bobo$444b2o34b2o$444b2o57b2o$429b2o72b2o$428bo2bo$427bob2o$427bo$426b2o$441b2o$441bo$442b3o24b2o42b2o6b2o$399b2o43bo11b2o11b2o23b2o18bo7bo$391b2o5bobo56bo36bo16b3o5b3o$391bobo4bo55b3o38b3o13bo7bo$393bo2b2ob4o51bo42bo$392b2obobobo2bo$393bobobobo73b2o$393bobob2o75bo54b2o$394bo76b3o50b2o3b2o$471bo52b2o$407b2o$398b2o7bo$380bo17b2o5bobo115b2o12b2o$380b3o22b2o117bo5b2o5bo$383bo137b3o6b2o6b3o$382b2o137bo18bo2$508b2o11bo$374b2o132b2o10bobo$374bo145bobo2b2o3bo$371b2obo20b2o122b2ob2o2bo2bobo$371bo2b3o4b2o13bo126bobo3bobo12b2o$372b2o3bo3b2o10b3o123b2obo2b4obo13bo$374b4o15bo125b2obobo3bo13bobo$374bo15b2obo129bobo3bo12b2o$375b3o12bobob2o128bobo3bo$378bo13bo3bo128bo3b2o$373b5o14b3o2bo152b2o$373bo21b3o153bo$375bo18bo156bobo$374b2o18b2o120b2o34b2o$516b2o$501b2o$500bo2bo$499bob2o70b2o$499bo73b2o$498b2o$384b2o127b2o$383bobo5b2o120bo$383bo7b2o121b3o24b2o$382b2o132bo11b2o11b2o$529bo$396bo129b3o$392b2obobo128bo$391bobobobo$388bo2bobobob2o146b2o$388b4ob2o2bo148bo$392bo4bobo143b3o$390bobo5b2o143bo$390b2o171b2o$563b2o8$546b2o11bo$546b2o10bobo$558bobo2b2o3bo$557b2ob2o2bo2bobo$561bobo3bobo$557b2obo2b4obo$557b2obobo3bo$561bobo3bo4bo17b2o$562bobo3bo3b3o7b2o7bo$563bo3b2o6bo6bo8bobo$574b2o4bobo9b2o$580b2o2$554b2o$554b2o57b2o$539b2o72b2o$538bo2bo$500bo11b2o23bob2o$499bobo10b2o23bo$491bo3b2o2bobo34b2o$490bobo2bo2b2ob2o48b2o$490bobo3bobo52bo$491bob4o2bob2o49b3o$493bo3bobob2o51bo$492bo3bobo$491bo3bobo$491b2o3bo$477bo90b2o$477b3o89bo$480bo85b3o3bob2o27b2o$479b2o23b2o60bo2b4ob2o27b2o$504b2o63bo$519b2o50b2ob2o2b2o6b2o$518bo2bo50bobo4bo6bobo17b2o11bo$519b2obo49bo2b4o9bo17b2o10bobo$522bo50bobo2bobo7b2o28bobo2b2o3bo$522b2o50bo4b2o36b2ob2o2bo2bobo$435bo31b2o38b2o112bobo3bobo12b2o24b2o$435b3o28bo2bo38bo49bo11b2o45b2obo2b4obo13bo25bo$438bo28b2o36b3o49bobo10b2o45b2obobo3bo13bobo23bobo$437b2o53b2o11bo43bo3b2o2bobo61bobo3bo12b2o24b2o9bo$492bo55bobo2bo2b2ob2o61bobo3bo46b3o$464b2o17b2obo6b3o52bobo3bobo66bo3b2o45bo$465bo17b2ob3o6bo53bob4o2bob2o87b2o24b2o$462b3o24bo61bo3bobob2o88bo$462bo20b2ob3o61bo3bobo92bobo$428bo55bobo62bo3bobo58b2o34b2o$428b3o23b2o22b2o4bobo62b2o3bo59b2o$431bo21bo2bo21bo6bo49bo63b2o$430b2o22b2o23b3o53b3o60bo2bo$481bo56bo58bob2o$537b2o23b2o33bo$562b2o32b2o$577b2o32b2o$576bo2bo31bo$577b2obo31b3o24b2o$580bo33bo11b2o11b2o$440b2o138b2o45bo$440b2o83b2o38b2o57b3o38b2o$524bo2bo38bo57bo34b2o4bobo$525b2o36b3o94bo6bo$550b2o11bo79b2o12b3o7b2o$550bo93bo12bo$522b2o17b2obo6b3o87b3o$523bo17b2ob3o6bo87bo$520b3o24bo$520bo20b2ob3o76bo11b2o$432b2o50bo57bobo77bobo10b2o$427b2o2bo2bo49b3o49b2o4bobo69bo3b2o2bobo$427bo4bobo52bo48bo6bo69bobo2bo2b2ob2o$424b2obo5bo52b2o49b3o73bobo3bobo$425bobob2o108bo74bob4o2bob2o$424bo2bo2bo185bo3bobob2o$424b2o2bo4bo181bo3bobo$429b5o180bo3bobo$614b2o3bo$428bob2o45bo122bo$428b2obo45b3o23b2o95b3o$480bo21bo2bo97bo$479b2o22b2o97b2o23b2o$627b2o$642b2o$641bo2bo$642b2obo$645bo$645b2o$590b2o38b2o$489b2o98bo2bo38bo$489b2o99b2o36b3o$615b2o11bo$615bo$587b2o17b2obo6b3o$588bo17b2ob3o6bo$585b3o24bo$585bo20b2ob3o$607bobo$601b2o4bobo$481b2o118bo6bo$476b2o2bo2bo118b3o$476bo4bobo120bo$473b2obo5bo$474bobob2o$473bo2bo2bo$473b2o2bo4bo$478b5o2$477bob2o$477b2obo7$530bo$530b3o$533bo$532b2o6$523bo$523b3o23b2o$526bo21bo2bo$525b2o22b2o8$535b2o$535b2o9$527b2o$522b2o2bo2bo$522bo4bobo$519b2obo5bo$520bobob2o$519bo2bo2bo$519b2o2bo4bo$524b5o2$523bob2o$523b2obo!", -349, -412)
gld_l_clock = g.parse("o$b2o$2o!", -332, -367)
gld_r_clock = g.parse("b2o$2o$2bo!", 309, 390)

def f(cells):
   return g.evolve(g.transform(cells, -1, 0, 0, -1, -1, 0), 2)

def add_shooter(cost, inserter_cells, left_g, right_g=[], flip=True):

   global shoot_defs

   g.new('')
   g.putcells(inserter_cells)
   g.putcells(left_g)
   g.putcells(right_g)
   g.run(2048)
   reaction_cells = g.getcells([-150,-150,300,300])
   g.run(512)

   if not all(g.getcell(x, y) for x, y in gld_pairs):
      g.fit()
      g.update()
      assert(False)

   stable_cells = set(zip(reaction_cells[::2], reaction_cells[1::2]))
   for _ in range(4):
      g.run(1)
      for i in range(0, len(reaction_cells), 2):
         tup = reaction_cells[i], reaction_cells[i+1]
         if tup in stable_cells and not g.getcell(*tup):
            stable_cells.remove(tup)

   stable_cells2 = []
   for x, y in stable_cells:
      stable_cells2.append(x)
      stable_cells2.append(y)
   stable_cells = stable_cells2

   tup = (cost, inserter_cells, left_g, right_g, reaction_cells, stable_cells)
   shoot_defs.append(tup)

   if flip:
      shoot_defs.append((cost,
                       f(inserter_cells),
                       f(right_g),
                       f(left_g),
                       f(reaction_cells),
                       f(stable_cells)))

def init_shooters():
   add_shooter(1, l_edge1, l_gld1)
   add_shooter(1, l_edge2, l_gld2)
   add_shooter(1, l_edge3, l_gld3)
   add_shooter(1, l_edge4, l_gld4)
   add_shooter(8, clock_insert, gld_l_clock, gld_r_clock, False)

init_location = 75
def is_there(x, y, gl):
   l = len(gl)
   for i in range(1, l, 2):
      xg = gl[i - 1]
      yg = gl[i]
      
      if g.getcell(x + xg, y + yg) == 0:
         return False
   
   for i in range(1, l, 2):
      xg = gl[i - 1]
      yg = gl[i]
      g.setcell(x + xg, y + yg, 0)
   return True
   

def is_there_glider(x, y):
   for i in range(4):
      gl = g.evolve(gld, i)
      
      if is_there(x, y, gl):
         return i
         
   return -1
   
def find_and_remove_all():
   cells = g.getcells(g.getrect())
   
   l = len(cells)
   res = []
   
   for i in range(1, l, 2):
      x = cells[i - 1]
      y = cells[i]
      
      for k in range(-1, 2):
         for l in range(-1, 2):
            idx = is_there_glider(x + k, y + l)
            if idx >= 0:
               res.append((x + k, y + l, idx))

   return res

def popcount(x):
   pop = 0
   while x:
      pop += x & 1
      x //= 2
   return pop

def extract_indexes(x):
   indexes = []
   idx = 0
   while x:
      if x & 1:
         indexes.append(idx)
      x //= 2
      idx += 1
   return indexes

def find_all_glider_idx(mask):
   
   idxs = extract_indexes(mask)
   idxs.sort(key=lambda idx: (1.01 * gliders_in[idx][0] + gliders_in[idx][1]))

#   shooters = range(6, 12) + range(6) + [12] if popcount(mask) % 2 else range(13)
   shooters = range(len(shoot_defs))
   copy_idxs = idxs[:]

   for edge_i in shooters:
      reaction_cells = shoot_defs[edge_i][4]
      stable_cells = shoot_defs[edge_i][5]

      for g_i in copy_idxs:
      
         g.new("")
 
         for g_j in idxs:
            x, y, idx = gliders_in[g_j]
            if g_j == g_i:
               g.putcells(g.evolve(reaction_cells, idx), x, y)
            else:
               g.putcells(g.evolve(gld, idx), x - 128, y + 128)

         g.setbase(8)
         g.setstep(3)
         g.step()
         
         x, y, _ = gliders_in[g_i]
         fail = False
         for i in range(0, len(stable_cells), 2):
            if not g.getcell(stable_cells[i] + x, stable_cells[i+1] + y):
               fail = True
               break
            g.setcell(stable_cells[i] + x, stable_cells[i+1] + y, 0)

         if not fail and len(g.getcells(ini_rect)) == 10 * len(idxs) and int(g.getpop()) == 5 * len(idxs):
            del copy_idxs[copy_idxs.index(g_i)]
            yield g_i,edge_i

def a_star_search():
   
   gen = 0
   start = 2 ** len(gliders_in) - 1
   frontier = [(popcount(start), gen, start)]
   cost = { start : 0 }
   prev = { start : None }
   
   while frontier:
      current = heapq.heappop(frontier)[2]
      g.show(str((popcount(current), cost[current])))
      if current == 0:
         break
      
      for g_i, edge_i in find_all_glider_idx(current):
         new_cost = cost[current] + shoot_defs[edge_i][0]
         new_mask = current ^ (2 ** g_i)
         if new_mask not in cost or new_cost < cost[new_mask]:
            cost[new_mask] = new_cost
            priority = new_cost + popcount(new_mask)
            gen -= 1
            heapq.heappush(frontier, (priority, gen, new_mask))
            prev[new_mask] = g_i, edge_i
         if shoot_defs[edge_i][0] == 1:
            break
            
   return prev

ini_rect = g.getrect()
gliders_in = find_and_remove_all()
init_shooters()
prev = a_star_search()

step_d = 250
total_d = 0

g.new("")

current = 0
start = 2 ** len(gliders_in) - 1

while current != start:

   i, edge_i = prev[current]
   current ^= 2 ** i

   x, y, idx = gliders_in[i]
   _, edge_shoot, left_g, right_g, _, _ = shoot_defs[edge_i]

   g.putcells(edge_shoot, x + total_d, y - total_d,)
   
   g.putcells(g.evolve(left_g, idx), x, y - 2 * total_d)
   g.putcells(g.evolve(right_g, idx), x + 2 * total_d, y)
      
   total_d += step_d

   g.fit()
   g.update()
