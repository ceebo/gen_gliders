import golly as g
import heapq

global ini_rect
global gliders_in

gld = g.parse("3o$2bo$bo!")

#ini_gld = g.parse("o$b2o$2o!", -90, 12)
#edge_shoot = g.parse("67b2o$67bobo$69bo$63b2o3bob2o$64bo3bo3bo$52b2o10bob2ob2obo$27b2o24bo11bobobobo$28bo13b2o6b3o$28bobo11b2o6bo$18bo10b2o$16b3o$15bo$15b2o$2o$bo$bob2o$2bo2bo$3b2o$18b2o$18b2o$56b2o$56b2o2$27bo3b2o$26bobo3bo5b2o3b2o$25bobo3bo7bo3bo$21b2obobo3bo5b3o5b3o$21b2obo2b4obo3bo9bo$25bobo3bobo$21b2ob2o2bo2bobo$22bobo2b2o3bo$10b2o10bobo$10b2o11bo!", -91, 8)

#ini_gld = g.parse("obo$b2o$bo!", -91, -15)
#edge_shoot = g.parse("$43b2o$43b2o5b2o$50b2o3$23bo5b2o17b2o$21b3o6bo17b2o$20bo9bobo21b2o$20b2o9b2o21b2o$5b2o$6bo$6bob2o$7bo2bo$8b2o$23b2o$23b2o4$32bo3b2o$31bobo3bo20bo$30bobo3bo19b3o$26b2obobo3bo19bo$26b2obo2b4obo17b2o$30bobo3bobo$26b2ob2o2bo2bobo$27bobo2b2o3bo$15b2o10bobo$15b2o11bo5$35b2o$35b2o9$50b2o$50b2o!", -90, -10)
#g.putcells(edge_shoot)
#g.putcells(ini_gld)

l_edge1 = g.parse("2$42b2o$42b2o5b2o$49b2o3$22bo5b2o17b2o$20b3o6bo17b2o$19bo9bobo21b2o$19b2o9b2o21b2o$4b2o$5bo$5bob2o$6bo2bo$7b2o$22b2o$22b2o4$31bo3b2o$30bobo3bo20bo$29bobo3bo19b3o$25b2obobo3bo19bo$25b2obo2b4obo17b2o$29bobo3bobo$25b2ob2o2bo2bobo$26bobo2b2o3bo$14b2o10bobo$14b2o11bo5$34b2o$34b2o9$49b2o$49b2o!", -117, 17)
l_gld1 = g.parse("obo$b2o$bo!", -119, 13)

l_edge2 = g.parse("41b2o$41b2o5b2o$48b2o3$21bo5b2o17b2o$19b3o6bo17b2o$18bo9bobo21b2o$18b2o9b2o21b2o$3b2o$4bo$4bob2o$5bo2bo$6b2o$21b2o$21b2o4$30bo3b2o$29bobo3bo$28bobo3bo$24b2obobo3bo$24b2obo2b4obo$28bobo3bobo$24b2ob2o2bo2bobo$25bobo2b2o3bo$13b2o10bobo$13b2o11bo2$59b2o$59bo$57bobo$57b2o$33b2o$33b2o6$35b2o$36bo$33b3o$33bo$34b2o$35bo$35bobo$36b2o5$34b2o$35bo$22b2o11bobo$23bo12b2o$23bobo$24b2o2b2o$28b2o4$23b2o4b2o$23b2o4b2o7$24b2o$23bobo$23bo$22b2o!", -86, 108 - 150)
l_gld2 = g.parse("obo$b2o$bo!", -89, 102 - 150)

l_edge3 = g.parse("2$43b2o$43b2o5b2o$50b2o3$23bo5b2o17b2o$21b3o6bo17b2o$20bo9bobo21b2o$20b2o9b2o21b2o$5b2o$6bo$6bob2o$7bo2bo$8b2o$23b2o$23b2o4$32bo3b2o$31bobo3bo$30bobo3bo$26b2obobo3bo$26b2obo2b4obo$30bobo3bobo$26b2ob2o2bo2bobo$27bobo2b2o3bo$15b2o10bobo$15b2o11bo2$61b2o$61bo$59bobo$59b2o$35b2o$35b2o6$37b2o$38bo$35b3o$35bo$36b2o$37bo$37bobo$38b2o5$36b2o$37bo$24b2o11bobo$25bo12b2o$25bobo$26b2o2b2o$30b2o4$25b2o4b2o$25b2o4b2o7$26b2o$25bobo$25bo$24b2o!", -88, 256 - 300)
l_gld3 = g.parse("$bobo$2b2o$2bo!", -90, 251-300)

l_edge4 = g.parse("12$69bo$67b3o$66bo$66b2o5$45bo$45b3o$48bo$47b2o$71b2o$28bo42b2o$28b3o$31bo50bo$18bo11b2o11b2o35b3o$16b3o24b2o34bo$15bo63b2o$15b2o$2o$bo$bob2o$2bo2bo$3b2o$18b2o$18b2o34b2o$53bobo$53bo$52b2o$27bo3b2o$26bobo3bo25b2o$25bobo3bo26b2o$21b2obobo3bo12b2o$21b2obo2b4obo10bo$25bobo3bobo10b3o$21b2ob2o2bo2bobo12bo$22bobo2b2o3bo$10b2o10bobo$10b2o11bo3b2o35b2o$27bobo35bo$28bo33b3o$62bo!", -108, 437-450)
l_gld4 = g.parse("$bo$2b2o$b2o!", -114, 453-450)

l_edge5 = g.parse("4$45bo$45b3o$41bo6bo$40bobo4b2o$40bobo$38b3ob2o20bo$37bo24b3o$31bo6b3ob2o17bo$31b3o6bob2o17b2o$34bo$21bo11b2o$19b3o36b2o$18bo38bo2bo$18b2o38b2o$3b2o$4bo$4bob2o$5bo2bo$6b2o$21b2o$21b2o23b2o$46bo$47b3o$49bo$30bo3b2o$29bobo3bo$28bobo3bo$24b2obobo3bo$24b2obo2b4obo$28bobo3bobo$24b2ob2o2bo2bobo$25bobo2b2o3bo$13b2o10bobo$13b2o11bo3b2o$30bobo$31bo!", -119, 635-600)
l_gld5 = g.parse("2$4bo$2bobo$3b2o!", -124, 636-600)

l_edge6 = g.parse("3$69b2o$69bobo$71bo$65b2o3bob2o$66bo3bo3bo$54b2o10bob2ob2obo$29b2o24bo11bobobobo$30bo13b2o6b3o$30bobo11b2o6bo$20bo10b2o$18b3o$17bo$17b2o$2b2o$3bo$3bob2o$4bo2bo$5b2o$20b2o$20b2o$58b2o$58b2o2$29bo3b2o$28bobo3bo5b2o3b2o$27bobo3bo7bo3bo$23b2obobo3bo5b3o5b3o$23b2obo2b4obo3bo9bo$27bobo3bobo$23b2ob2o2bo2bobo$24bobo2b2o3bo$12b2o10bobo$12b2o11bo!", -115, 777-750)
l_gld6 = g.parse("2$2bo$3b2o$2b2o!", -120, 776-750)

r_edge1 = g.parse("2$30b2o$29bo2bo$30bobo$29b2o2b2o$31b2o2bo$29b2o3b2o$30bo$29bo$30b3o$32bo6$14b2o$14b2o3$29b2o$28bobo$28bo$27b2o4$8b2o$9bo$9bobo$10b2o15b2o$27b2o3$10b2o$9bobo$9bo$8b2o3$6b2o$5bo2bo2b2o$6b2o2bobo$8b2o16b2o$8bo17bo$5b2obo2bo15b3o$5bob2obobo16bo$9bobo$6b2o2bo$4b3ob2o$3bo$4b3ob2o$6bob2o2$16b2o$16b2o7b2o$25bo$23bobo$23b2o4$3b2o$3b2o5$19bo$18bobo$18bobo$19bo$20b3o$22bo!", -64, 41)
r_gld1 = g.parse("b2o$2o$2bo!", -30, 118)

r_edge2 = g.parse("$30b2o$30bo$28bobo$28b2o$24bo$23bobo$23bobo$24bo8$13b2o$14bo18b2o$14bobo16bobo$15b2o18bo$35b2o2$28b2obo$28b2ob3o$34bo$28b2ob3o$29bobo$29bobo$30bo$6b2o$5bo2bo2b2o$6b2o2bobo13b2o$8b2o16bobo$2bo5bo19bo$bobob2obo2bo16b2o$2b2obob2obobo$9bobo$6b2o2bo$4b3ob2o$3bo$4b3ob2o$6bob2o2$16b2o$16b2o7b2o$25bo$23bobo$23b2o4$3b2o$3b2o5$19bo$18bobo$18bobo$19bo$20b3o$22bo!", 76-150, 56)
r_gld2 = g.parse("2o$obo$o!", 111-150, 121)

r_edge3 = g.parse("3$34b2o$34bo$32bobo$32b2o7$37b2o$37b2o2$49b2o$49bo$47bobo$47b2o$10b2o$9bobo$9bo$8b2o3$18b2o$18b2o3$23b2o$24bo$21b3o$21bo4$39b2o$39bobo$14b2o25bo$15bo25b2o$15bobo15b2o$16b2o15b2o10$14b2o$13bo2bo2b2o$14b2o2bobo13b2o$16b2o16bobo$10bo5bo19bo$9bobob2obo2bo16b2o$10b2obob2obobo$17bobo$14b2o2bo$12b3ob2o$11bo$12b3ob2o$14bob2o2$24b2o$24b2o7b2o$33bo$31bobo$31b2o4$11b2o$11b2o5$27bo$26bobo$26bobo$27bo$28b3o$30bo!", 252-300, 25)
r_gld3 = g.parse("2$2b2o$b2o$3bo!", 293-300, 111)

r_edge4 = g.parse("11$61bo$59b3o$58bo$58b2o4$83b2o$83b2o3$89b2o$89b2o$85b2o$85b2o4$90b2o$90b2o4$35b2o6b2o$35bo7bo5b2o15b2o$36b3o5b3obobo14bo2bo2b2o$38bo7bobo7b2o8b2o2bobo$47b2o7b2o10b2o$68bo$65b2obo2bo$27b2o36bob2obobo10b2o$27b2o3b2o35bobo11bo$32b2o32b2o2bo13b3o$64b3ob2o16bo$63bo$19b2o12b2o29b3ob2o$20bo6b2o4bo32bob2o$17b3o7b2o5b3o$17bo18bo39b2o$76b2o7b2o$85bo$83bobo$83b2o4$63b2o$63b2o5$79bo$78bobo$78bobo$79bo$80b3o$82bo!", 402-450, 17)
r_gld4 = g.parse("bo$2o$obo!", 497-450, 88)

r_edge5 = g.parse("10$45bo$43b3o$42bo$42b2o4$67b2o$67b2o3$73b2o$73b2o$69b2o$69b2o4$74b2o$74b2o4$19b2o6b2o$19bo7bo5b2o15b2o$20b3o5b3obobo14bo2bo2b2o$22bo7bobo7b2o8b2o2bobo$31b2o7b2o10b2o$52bo$49b2obo2bo$11b2o36bob2obobo10b2o$11b2o3b2o35bobo11bo$16b2o32b2o2bo13b3o$48b3ob2o16bo$47bo$3b2o12b2o29b3ob2o$4bo6b2o4bo32bob2o$b3o7b2o5b3o$bo18bo39b2o$60b2o7b2o$69bo$67bobo$67b2o4$47b2o$47b2o5$63bo$62bobo$62bobo$63bo$64b3o$66bo!", 568-600, 18)
r_gld5 = g.parse("bo$2o$obo!", 647-600, 88)

r_edge6 = g.parse("5$30b2o$30bo$28bobo$28b2o13b2o$43b2o3$7b2o40b2o$7b2o40b2o$45b2o$45b2o4$50b2o$50b2o5$26b2o$25bo2bo2b2o$17b2o7b2o2bobo$17b2o9b2o$28bo$25b2obo2bo$25bob2obobo10b2o$29bobo11bo$26b2o2bo13b3o$24b3ob2o16bo$23bo$24b3ob2o$26bob2o2$36b2o$36b2o7b2o$45bo$43bobo$43b2o4$23b2o$23b2o5$39bo$38bobo$38bobo$39bo$40b3o$42bo!", 681-750, 57)
r_gld6 = g.parse("bo$2o$obo!", 736-750, 118)

l_edge = [l_edge1,l_edge2,l_edge3,l_edge4,l_edge5,l_edge6,r_edge1,r_edge2,r_edge3,r_edge4,r_edge5,r_edge6]
l_gld = [l_gld1,l_gld2,l_gld3,l_gld4,l_gld5,l_gld6,r_gld1,r_gld2,r_gld3,r_gld4,r_gld5,r_gld6]

clock_insert = g.parse("52$306bob2o$306b2obo2$304b5o$304bo4bo2b2o$307bo2bo2bo$307b2obobo$304bo5bob2o$303bobo4bo$303bo2bo2b2o$304b2o9$296b2o$296b2o8$282b2o22b2o$281bo2bo21bo$282b2o23b3o$309bo6$299b2o$299bo$300b3o$302bo7$352bob2o$352b2obo2$350b5o$350bo4bo2b2o$353bo2bo2bo$353b2obobo$350bo5bob2o$228bo120bobo4bo$228b3o118bo2bo2b2o$224bo6bo118b2o$223bobo4b2o$223bobo$221b3ob2o20bo$220bo24b3o$214bo6b3ob2o17bo$214b3o6bob2o17b2o$217bo$204bo11b2o$202b3o36b2o99b2o$201bo38bo2bo98b2o$201b2o38b2o$186b2o$187bo$187bob2o$188bo2bo$189b2o$204b2o$204b2o23b2o97b2o22b2o$229bo97bo2bo21bo$230b3o95b2o23b3o45bob2o$232bo122bo45b2obo$213bo3b2o$212bobo3bo180b5o$211bobo3bo181bo4bo2b2o$207b2obobo3bo185bo2bo2bo$207b2obo2b4obo74bo108b2obobo$211bobo3bobo73b3o49b2o52bo5bob2o$207b2ob2o2bo2bobo69bo6bo48bo52bobo4bo$208bobo2b2o3bo69bobo4b2o49b3o49bo2bo2b2o$196b2o10bobo77bobo57bo50b2o$196b2o11bo76b3ob2o20bo$285bo24b3o$191bo87bo6b3ob2o17bo$189b3o87b3o6bob2o17b2o$175bo12bo93bo$164b2o7b3o12b2o79bo11b2o$165bo6bo94b3o36b2o$165bobo4b2o34bo57bo38bo2bo$166b2o38b3o57b2o38b2o83b2o$205bo45b2o138b2o$192b2o11b2o11bo33bo$192b2o24b3o31bob2o$221bo31bo2bo$220b2o32b2o$235b2o32b2o$235bo33b2o23b2o$232b2obo58bo56bo$231bo2bo60b3o53b3o23b2o22b2o$232b2o63bo49bo6bo21bo2bo21bo$217b2o59bo3b2o62bobo4b2o22b2o23b3o$181b2o34b2o58bobo3bo62bobo55bo$181bobo92bobo3bo61b3ob2o20bo$183bo88b2obobo3bo61bo24b3o$157b2o24b2o87b2obo2b4obo53bo6b3ob2o17bo$158bo45b2o3bo66bobo3bobo52b3o6bob2o17b2o$155b3o46bo3bobo61b2ob2o2bo2bobo55bo$155bo9b2o24b2o12bo3bobo61bobo2b2o3bo43bo11b2o53b2o$164bobo23bobo13bo3bobob2o45b2o10bobo49b3o36b2o28bo$164bo25bo13bob4o2bob2o45b2o11bo49bo38bo2bo28b3o$163b2o24b2o12bobo3bobo112b2o38b2o31bo$203bobo2bo2b2ob2o36b2o4bo50b2o$204bo3b2o2bobo28b2o7bobo2bobo50bo$212bobo10b2o17bo9b4o2bo49bob2o$213bo11b2o17bobo6bo4bobo50bo2bo$245b2o6b2o2b2ob2o50b2o$263bo63b2o$228b2o27b2ob4o2bo60b2o23b2o$228b2o27b2obo3b3o85bo$263bo89b3o$263b2o90bo$336bo3b2o$335bobo3bo$334bobo3bo$278bo51b2obobo3bo$278b3o49b2obo2b4obo$281bo52bobo3bobo$280b2o48b2ob2o2bo2bobo$295b2o34bobo2b2o3bo$295bo23b2o10bobo$292b2obo23b2o11bo$291bo2bo$218b2o72b2o$218b2o57b2o$277b2o2$251b2o$239b2o9bobo4b2o$239bobo8bo6bo6b2o3bo$241bo7b2o7b3o3bo3bobo$241b2o17bo4bo3bobo$266bo3bobob2o$264bob4o2bob2o$263bobo3bobo$263bobo2bo2b2ob2o$264bo3b2o2bobo$272bobo10b2o$273bo11b2o8$268b2o$268b2o$289bo$287b3o$286bo$286b2o165b2o$445b2o5bobo$306bo138bobo4bo$304b3o140bo2b2ob4o$303bo142b2obobobo2bo$290b2o11b2o11bo130bobobobo$290b2o24b3o128bobob2o$319bo128bo$318b2o$333b2o126b2o$258b2o73bo118b2o7bo$258b2o70b2obo118b2o5bobo$329bo2bo126b2o$330b2o$315b2o$279b2o34b2o$279bobo$281bo$281b2o$302b2o3bo141b2o18b2o$302bo3bobo141bo18bo$289b2o12bo3bobo137b3o21bo$288bobo13bo3bobob2o133bo2b3o14b5o$288bo13bob4o2bob2o135bo2bo13bo$287b2o12bobo3bobo138b2o2bobo12b3o$301bobo2bo2b2ob2o139b2o15bo$302bo3b2o2bobo154b4o$310bobo10b2o137b2o3bo3b2o$311bo11b2o137b2o4b3o2bo$470bob2o$447bo22bo$307bo18bo118b3o21b2o$307b3o6b2o6b3o117bo$310bo5b2o5bo120b2o$309b2o12b2o136b2o$461bo$462b3o$322b2o52bo87bo$317b2o3b2o50b3o$317b2o54bo$373b2o59b2o$433bobo5b2o$350bo42bo39bo7b2o$328bo7bo13b3o38b3o38b2o$326b3o5b3o16bo36bo$325bo7bo18b2o23b2o11b2o11bo42bo$325b2o6b2o42b2o24b3o36b2obobo$406bo34bobobobo$405b2o31bo2bobobob2o$420b2o16b4ob2o2bo$420bo21bo4bobo$417b2obo19bobo5b2o$416bo2bo20b2o$343b2o72b2o$343b2o57b2o$366b2o34b2o$366bobo$368bo$356b2o10b2o$356bo32b2o3bo$346b2o9b3o29bo3bobo$347bo11bo16b2o12bo3bobo$346bo28bobo13bo3bobob2o$346b2o27bo13bob4o2bob2o$374b2o12bobo3bobo$388bobo2bo2b2ob2o$389bo3b2o2bobo$397bobo10b2o$398bo11b2o220$431b2o11bo$431b2o10bobo$443bobo2b2o3bo$442b2ob2o2bo2bobo$446bobo3bobo12b2o$442b2obo2b4obo13bo27b2o$442b2obobo3bo13bobo28bo$446bobo3bo12b2o16bo11bo$447bobo3bo29b3o9b2o$448bo3b2o32bo$473b2o10b2o$474bo$474bobo$439b2o34b2o$439b2o57b2o$424b2o72b2o$423bo2bo$422bob2o$422bo$421b2o$436b2o$436bo$437b3o24b2o42b2o6b2o$394b2o43bo11b2o11b2o23b2o18bo7bo$386b2o5bobo56bo36bo16b3o5b3o$386bobo4bo55b3o38b3o13bo7bo$388bo2b2ob4o51bo42bo$387b2obobobo2bo$388bobobobo73b2o$388bobob2o75bo54b2o$389bo76b3o50b2o3b2o$466bo52b2o$402b2o$393b2o7bo$375bo17b2o5bobo115b2o12b2o$375b3o22b2o117bo5b2o5bo$378bo137b3o6b2o6b3o$377b2o137bo18bo2$503b2o11bo$369b2o132b2o10bobo$369bo145bobo2b2o3bo$366b2obo20b2o122b2ob2o2bo2bobo$366bo2b3o4b2o13bo126bobo3bobo12b2o$367b2o3bo3b2o10b3o123b2obo2b4obo13bo$369b4o15bo125b2obobo3bo13bobo$369bo15b2obo129bobo3bo12b2o$370b3o12bobob2o128bobo3bo$373bo13bo3bo128bo3b2o$368b5o14b3o2bo152b2o$368bo21b3o153bo$370bo18bo156bobo$369b2o18b2o120b2o34b2o$511b2o$496b2o$495bo2bo$494bob2o70b2o$494bo73b2o$493b2o$379b2o127b2o$378bobo5b2o120bo$378bo7b2o121b3o24b2o$377b2o132bo11b2o11b2o$524bo$391bo129b3o$387b2obobo128bo$386bobobobo$383bo2bobobob2o146b2o$383b4ob2o2bo148bo$387bo4bobo143b3o$385bobo5b2o143bo$385b2o171b2o$558b2o8$541b2o11bo$541b2o10bobo$553bobo2b2o3bo$552b2ob2o2bo2bobo$556bobo3bobo$552b2obo2b4obo$552b2obobo3bo$556bobo3bo4bo17b2o$557bobo3bo3b3o7b2o7bo$558bo3b2o6bo6bo8bobo$569b2o4bobo9b2o$575b2o2$549b2o$549b2o57b2o$534b2o72b2o$533bo2bo$495bo11b2o23bob2o$494bobo10b2o23bo$486bo3b2o2bobo34b2o$485bobo2bo2b2ob2o48b2o$485bobo3bobo52bo$486bob4o2bob2o49b3o$488bo3bobob2o51bo$487bo3bobo$486bo3bobo$486b2o3bo$472bo90b2o$472b3o89bo$475bo85b3o3bob2o27b2o$474b2o23b2o60bo2b4ob2o27b2o$499b2o63bo$514b2o50b2ob2o2b2o6b2o$513bo2bo50bobo4bo6bobo17b2o11bo$514b2obo49bo2b4o9bo17b2o10bobo$517bo50bobo2bobo7b2o28bobo2b2o3bo$517b2o50bo4b2o36b2ob2o2bo2bobo$430bo31b2o38b2o112bobo3bobo12b2o24b2o$430b3o28bo2bo38bo49bo11b2o45b2obo2b4obo13bo25bo$433bo28b2o36b3o49bobo10b2o45b2obobo3bo13bobo23bobo$432b2o53b2o11bo43bo3b2o2bobo61bobo3bo12b2o24b2o9bo$487bo55bobo2bo2b2ob2o61bobo3bo46b3o$459b2o17b2obo6b3o52bobo3bobo66bo3b2o45bo$460bo17b2ob3o6bo53bob4o2bob2o87b2o24b2o$457b3o24bo61bo3bobob2o88bo$457bo20b2ob3o61bo3bobo92bobo$423bo55bobo62bo3bobo58b2o34b2o$423b3o23b2o22b2o4bobo62b2o3bo59b2o$426bo21bo2bo21bo6bo49bo63b2o$425b2o22b2o23b3o53b3o60bo2bo$476bo56bo58bob2o$532b2o23b2o33bo$557b2o32b2o$572b2o32b2o$571bo2bo31bo$572b2obo31b3o24b2o$575bo33bo11b2o11b2o$435b2o138b2o45bo$435b2o83b2o38b2o57b3o38b2o$519bo2bo38bo57bo34b2o4bobo$520b2o36b3o94bo6bo$545b2o11bo79b2o12b3o7b2o$545bo93bo12bo$517b2o17b2obo6b3o87b3o$518bo17b2ob3o6bo87bo$515b3o24bo$515bo20b2ob3o76bo11b2o$427b2o50bo57bobo77bobo10b2o$422b2o2bo2bo49b3o49b2o4bobo69bo3b2o2bobo$422bo4bobo52bo48bo6bo69bobo2bo2b2ob2o$419b2obo5bo52b2o49b3o73bobo3bobo$420bobob2o108bo74bob4o2bob2o$419bo2bo2bo185bo3bobob2o$419b2o2bo4bo181bo3bobo$424b5o180bo3bobo$609b2o3bo$423bob2o45bo122bo$423b2obo45b3o23b2o95b3o$475bo21bo2bo97bo$474b2o22b2o97b2o23b2o$622b2o$637b2o$636bo2bo$637b2obo$640bo$640b2o$585b2o38b2o$484b2o98bo2bo38bo$484b2o99b2o36b3o$610b2o11bo$610bo$582b2o17b2obo6b3o$583bo17b2ob3o6bo$580b3o24bo$580bo20b2ob3o$602bobo$596b2o4bobo$476b2o118bo6bo$471b2o2bo2bo118b3o$471bo4bobo120bo$468b2obo5bo$469bobob2o$468bo2bo2bo$468b2o2bo4bo$473b5o2$472bob2o$472b2obo7$525bo$525b3o$528bo$527b2o6$518bo$518b3o23b2o$521bo21bo2bo$520b2o22b2o8$530b2o$530b2o9$522b2o$517b2o2bo2bo$517bo4bobo$514b2obo5bo$515bobob2o$514bo2bo2bo$514b2o2bo4bo$519b5o2$518bob2o$518b2obo!", -519, -289)
gld_r_clock = g.parse("b2o$2o$2bo!", 119, 390)
gld_l_clock = g.parse("o$b2o$2o!", -332, -177)

for i in range(6):
   l_gld[i] = g.transform(l_gld[i], -512, -512)
   l_gld[i + 6] = g.transform(l_gld[i+6], 512, 512)


gld_clock = []
gld_clock.extend(gld_l_clock)
gld_clock.extend(gld_r_clock)


l_edge.append(clock_insert)
l_gld.append(gld_clock)

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
   

def   is_there_glider(x, y):
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

   shooters = range(len(l_edge)-2, 0, -1) + [len(l_edge)-1] if popcount(mask) % 2 else range(len(l_edge))
   copy_idxs = idxs[:]

   for edge_i in shooters:
      edge_shoot = l_edge[edge_i]
      ini_gld = l_gld[edge_i]

      for g_i in copy_idxs:
      
         g.new("")
         step_d = 128
         x, y, idx = gliders_in[g_i]
         g.putcells(edge_shoot, x, y)
         g.putcells(g.evolve(ini_gld, idx), x, y)

         for g_j in idxs:
            if g_j == g_i:
               continue
               
            x, y, idx = gliders_in[g_j]
            g.putcells(g.evolve(gld, idx), x - step_d - 512, y + step_d + 512)

         pop = int(g.getpop())
         g.setbase(8)
         g.setstep(3)
         g.step()
         g.step()
         g.step()
         g.step()
         g.step()
         g.step()
         g.step()
         
         if 10 * len(idxs) == len(g.getcells([ini_rect[0] + 2 * step_d, ini_rect[1] - 2 * step_d, ini_rect[2], ini_rect[3]])) and (pop ==  int(g.getpop()) or pop - 5 ==  int(g.getpop())):
            del copy_idxs[copy_idxs.index(g_i)]
            yield g_i,edge_i

def recursive_search(mask):

   if mask == 0:
      return []

   g.show("remains glider %d" % popcount(mask))
   g.update()
   
   for g_i,edge_i in find_all_glider_idx(mask):
   
      recurse_seq = recursive_search(mask ^ (2 ** g_i))
         
      if recurse_seq != False:
         return [(g_i, edge_i)] + recurse_seq
         
   return False
         
def a_star_search():
   
   gen = 0
   start = 2 ** len(gliders_in) - 1
   frontier = [(popcount(start), gen, start)]
   came_from = { start : None }
   cost = { start : 0 }
   
   while frontier:
      current = heapq.heappop(frontier)[2]
      g.show(str((popcount(current), cost[current])))
      if current == 0:
         break
      
      for g_i, edge_i in find_all_glider_idx(current):
         new_cost = cost[current] + (1 if edge_i < 12 else 2)
         new_mask = current ^ (2 ** g_i)
         if new_mask not in cost or new_cost < cost[new_mask]:
            cost[new_mask] = new_cost
            priority = new_cost + popcount(new_mask)
            gen -= 1
            heapq.heappush(frontier, (priority, gen, new_mask))
            came_from[new_mask] = g_i, edge_i
         if edge_i < 12:
            break
            
   return came_from, cost

ini_rect = g.getrect()
gliders_in = find_and_remove_all()
#a_star_search()

seq = recursive_search(2 ** len(gliders_in) - 1)

g.show(str(seq))

if seq == False:
   g.new("")
   for x, y, idx in gliders_in:
      g.putcells(g.evolve(gld, idx), x, y)
   g.exit("Failed to solve")

step_d = 150

for i,edge_i in seq:
   if edge_i == 12:
      step_d = 250
      
total_d = len(gliders_in) * step_d
g.new("")
total_l = total_d
total_r = total_d

for i,edge_i in seq:
   x, y, idx = gliders_in[i]
   edge_shoot = l_edge[edge_i]
   ini_gld = l_gld[edge_i]

   g.putcells(edge_shoot, x + total_d, y - total_d,)
   
   if edge_i < 6:
      g.putcells(g.evolve(ini_gld, idx), x, y - 2 * total_d)
   elif edge_i < 12:   
      g.putcells(g.evolve(ini_gld, idx), x + 2 * total_d, y)
   else:
      pass
      g.putcells(g.evolve(gld_r_clock, idx), x + 2 * total_d, y)
      g.putcells(g.evolve(gld_l_clock, idx),  x, y - 2 * total_d)
      
   total_d -= step_d

