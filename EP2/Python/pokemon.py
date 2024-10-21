import os
!pip install neo4j
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"  # Altere para o URI do seu servidor Neo4j
username = "neo4j"             # Usuário padrão do Neo4J
password = "GraphpokeEp2"     # Senha que usei no meu Neo4J

driver = GraphDatabase.driver(uri, auth=(username, password))

#Vai acionar a query via python
query = """

CREATE CONSTRAINT IF NOT EXISTS FOR (p:Pokemon) REQUIRE (p.Tipo) IS UNIQUE;
CREATE INDEX IF NOT EXISTS FOR (p:Pokemon) ON (p.Name, p.Evolucao, p.Cor, p.PesoKg);

CREATE CONSTRAINT IF NOT EXISTS FOR (e:Elemento) REQUIRE (e.Tipo) IS UNIQUE;
CREATE INDEX IF NOT EXISTS FOR (e:Elemento) ON (e.Name);

CREATE CONSTRAINT IF NOT EXISTS FOR (h:Habilidade) REQUIRE (h.Tipo) IS UNIQUE;
CREATE INDEX IF NOT EXISTS FOR (h:Habilidade) ON (h.Name);

CREATE (Pikachu:Pokemon {Tipo: 'Pikachu', Nome: 'Pikachu', Evolucao: 'Raichu', Cor: 'Amarelo', PesoKg: '6'});
CREATE (Raichu:Pokemon {Tipo: 'Raichu', Nome: 'Raichu', Elemento: 'Elétrico', Evolucao: 'N/A', Habilidade: 'Static', Cor: 'Amarelo', PesoKg: '30'});

CREATE (Bulbasaur:Pokemon {Tipo: 'Bulbasaur', Evolucao: 'Ivysaur', Cor: 'Verde', PesoKg: '7'});
CREATE (Ivysaur:Pokemon {Tipo: 'Ivysaur', Evolucao: 'Venosaur', Cor: 'Verde', PesoKg: '13'});
CREATE (Venosaur:Pokemon {Tipo: 'Venosaur', Evolucao: 'N/A', Cor: 'Verde', PesoKg: '100'});

CREATE (Charmander:Pokemon {Tipo: 'Charmander', Evolucao: 'Charmeleon', Cor: 'Laranja', PesoKg: '9'});
CREATE (Charmeleon:Pokemon {Tipo: 'Charmeleon', Evolucao: 'Charizard', Cor: 'Laranja', PesoKg: '19'});
CREATE (Charizard:Pokemon {Tipo: 'Charizard', Evolucao: 'N/A', Cor: 'Laranja', PesoKg: '90'});

CREATE (Squirtle:Pokemon {Tipo: 'Squirtle', Evolucao: 'Wartotle', Cor: 'Azul', PesoKg: '9'});
CREATE (Wartotle:Pokemon {Tipo: 'Wartotle', Evolucao: 'Blastoise', Cor: 'Azul', PesoKg: '23'});
CREATE (Blastoise:Pokemon {Tipo: 'Blastoise', Evolucao: 'N/A', Cor: 'Azul', PesoKg: '86'});

CREATE (Shellder:Pokemon {Tipo: 'Shellder', Evolucao: 'Cloyster', Cor: 'Roxo', PesoKg: '4'});
CREATE (Cloyster:Pokemon {Tipo: 'Cloyster', Evolucao: 'N/A', Cor: 'Roxo', PesoKg: '4'});

CREATE (Diglett:Pokemon {Tipo: 'Diglett', Evolucao: 'Dugtrio', Cor: 'Marrom', PesoKg: '1'});
CREATE (Dugtrio:Pokemon {Tipo: 'Dugtrio', Evolucao: 'N/A', Cor: 'Marrom', PesoKg: '33'});

CREATE (Fogo:Elemento {Tipo: 'Fogo', Name: 'Fogo'});
CREATE (Agua:Elemento {Tipo: 'Agua', Name: 'Agua'});
CREATE (Terra:Elemento {Tipo: 'Terra', Name: 'Terra'});
CREATE (Gelo:Elemento {Tipo: 'Gelo', Name: 'Gelo'});
CREATE (Grama:Elemento {Tipo: 'Grama', Name: 'Grama'});
CREATE (Veneno:Elemento {Tipo: 'Veneno', Name: 'Veneno'});
CREATE (Voador:Elemento {Tipo: 'Voador', Name: 'Voador'});
CREATE (Eletrico:Elemento {Tipo: 'Eletrico', Name: 'Eletrico'});

CREATE (Overgrow:Habilidade {Tipo: 'Overgrow', Name: 'Overgrow'});
CREATE (Blaze:Habilidade {Tipo: 'Blaze', Name: 'Blaze'});
CREATE (Torrent:Habilidade {Tipo: 'Torrent', Name: 'Torrent'});
CREATE (Static:Habilidade {Tipo: 'Static', Name: 'Static'});
CREATE (SandVeil:Habilidade {Tipo: 'SandVeil', Name: 'SandVeil'});
CREATE (ShellArmor:Habilidade {Tipo: 'ShellArmor', Name: 'ShellArmor'});

MATCH (pi:Pokemon {Tipo: 'Pikachu'}), (ra:Pokemon {Tipo: 'Raichu'})
CREATE (pi)-[:Evolucao]->(ra);

MATCH (bu:Pokemon {Tipo: 'Bulbasaur'}), (iv:Pokemon {Tipo: 'Ivysaur'}), (ve:Pokemon {Tipo: 'Venosaur'})
CREATE (bu)-[:Evolucao]->(iv),
       (iv)-[:Evolucao]->(ve);

MATCH (cm:Pokemon {Tipo: 'Charmander'}), (cml:Pokemon {Tipo: 'Charmeleon'}), (chz:Pokemon {Tipo: 'Charizard'})
CREATE (cm)-[:Evolucao]->(cml),
       (cml)-[:Evolucao]->(chz);

MATCH (sq:Pokemon {Tipo: 'Squirtle'}), (war:Pokemon {Tipo: 'Wartotle'}), (bls:Pokemon {Tipo: 'Blastoise'})
CREATE (sq)-[:Evolucao]->(war),
       (war)-[:Evolucao]->(bls);

MATCH (sh:Pokemon {Tipo: 'Shellder'}), (cl:Pokemon {Tipo: 'Cloyster'})
CREATE (sh)-[:Evolucao]->(cl);

MATCH (dig:Pokemon {Tipo: 'Diglett'}), (dug:Pokemon {Tipo: 'Dugtrio'})
CREATE (dig)-[:Evolucao]->(dug);

MATCH (pi:Pokemon {Tipo: 'Pikachu'}), (ra:Pokemon {Tipo: 'Raichu'}), (el:Elemento {Tipo: 'Eletrico'})
CREATE (pi)-[:Elemento]->(el),
       (ra)-[:Elemento]->(el);

MATCH (bu:Pokemon {Tipo: 'Bulbasaur'}), (iv:Pokemon {Tipo: 'Ivysaur'}), (ve:Pokemon {Tipo: 'Venosaur'}), 
      (gr:Elemento {Tipo: 'Grama'}), (po:Elemento {Tipo: 'Veneno'})
CREATE (bu)-[:Elemento]->(gr), (bu)-[:Elemento]->(po),
       (iv)-[:Elemento]->(gr), (iv)-[:Elemento]->(po),
       (ve)-[:Elemento]->(gr), (ve)-[:Elemento]->(po);

MATCH (cm:Pokemon {Tipo: 'Charmander'}), (cml:Pokemon {Tipo: 'Charmeleon'}), (chz:Pokemon {Tipo: 'Charizard'}),
      (fo:Elemento {Tipo: 'Fogo'}), (voa:Elemento {Tipo: 'Voador'})
CREATE (cm)-[:Elemento]->(fo),
       (cml)-[:Elemento]->(fo),
       (chz)-[:Elemento]->(fo), (chz)-[:Elemento]->(voa);

MATCH (sq:Pokemon {Tipo: 'Squirtle'}), (war:Pokemon {Tipo: 'Wartotle'}), (bls:Pokemon {Tipo: 'Blastoise'}), (ag:Elemento {Tipo: 'Agua'})
CREATE (sq)-[:Elemento]->(ag),
       (war)-[:Elemento]->(ag),
       (bls)-[:Elemento]->(ag);

MATCH (sh:Pokemon {Tipo: 'Shellder'}), (cl:Pokemon {Tipo: 'Cloyster'}), (ag:Elemento {Tipo: 'Agua'}), (ge:Elemento {Tipo: 'Gelo'})
CREATE (sh)-[:Elemento]->(ag),
       (cl)-[:Elemento]->(ag), (cl)-[:Elemento]->(ge);

MATCH (dig:Pokemon {Tipo: 'Diglett'}), (dug:Pokemon {Tipo: 'Dugtrio'}), (te:Elemento {Tipo: 'Terra'})
CREATE (dig)-[:Elemento]->(te),
       (dug)-[:Elemento]->(te);

MATCH (bu:Pokemon {Tipo: 'Bulbasaur'}), (iv:Pokemon {Tipo: 'Ivysaur'}), (ve:Pokemon {Tipo: 'Venosaur'}), (ov:Habilidade {Tipo: 'Overgrow'})
CREATE (bu)-[:Habilidade]->(ov),
       (iv)-[:Habilidade]->(ov),
       (ve)-[:Habilidade]->(ov);

MATCH (cm:Pokemon {Tipo: 'Charmander'}), (cml:Pokemon {Tipo: 'Charmeleon'}), (chz:Pokemon {Tipo: 'Charizard'}), (blz:Habilidade {Tipo: 'Blaze'})
CREATE (cm)-[:Habilidade]->(blz),
       (cml)-[:Habilidade]->(blz),
       (chz)-[:Habilidade]->(blz);

MATCH (sq:Pokemon {Tipo: 'Squirtle'}), (war:Pokemon {Tipo: 'Wartotle'}), (bls:Pokemon {Tipo: 'Blastoise'}), (to:Habilidade {Tipo: 'Torrent'})
CREATE (sq)-[:Habilidade]->(to),
       (war)-[:Habilidade]->(to),
       (bls)-[:Habilidade]->(to);

MATCH (pi:Pokemon {Tipo: 'Pikachu'}), (ra:Pokemon {Tipo: 'Raichu'}), (st:Habilidade {Tipo: 'Static'})
CREATE (pi)-[:Habilidade]->(st),
       (ra)-[:Habilidade]->(st);

MATCH (dig:Pokemon {Tipo: 'Diglett'}), (dug:Pokemon {Tipo: 'Dugtrio'}), (sv:Habilidade {Tipo: 'SandVeil'})
CREATE (dig)-[:Habilidade]->(sv),
       (dug)-[:Habilidade]->(sv);

MATCH (sh:Pokemon {Tipo: 'Shellder'}), (cl:Pokemon {Tipo: 'Cloyster'}), (sa:Habilidade {Tipo: 'ShellArmor'})
CREATE (sh)-[:Habilidade]->(sa),
       (cl)-[:Habilidade]->(sa);

MATCH (fo:Elemento {Tipo:'Fogo'}), (gr:Elemento {Tipo:'Grama'})
CREATE (fo)-[:Forca]->(gr);

MATCH (gr:Elemento {Tipo:'Grama'}), (ag:Elemento {Tipo:'Agua'}), (te:Elemento {Tipo:'Terra'})
CREATE (gr)-[:Forca]->(ag),
       (gr)-[:Forca]->(te);

MATCH (ag:Elemento {Tipo:'Agua'}), (te:Elemento {Tipo:'Terra'}), (fo:Elemento {Tipo:'Fogo'})
CREATE (ag)-[:Forca]->(te),
       (ag)-[:Forca]->(fo);

MATCH (te:Elemento {Tipo:'Terra'}), (el:Elemento {Tipo:'Eletrico'}), (fo:Elemento {Tipo:'Fogo'})
CREATE (te)-[:Forca]->(el),
       (te)-[:Forca]->(fo);

MATCH (ge:Elemento {Tipo:'Gelo'}), (te:Elemento {Tipo:'Terra'}), (voa:Elemento {Tipo:'Voador'})
CREATE (ge)-[:Forca]->(te),
       (ge)-[:Forca]->(voa);

MATCH (po:Elemento {Tipo:'Veneno'}), (gr:Elemento {Tipo:'Grama'})
CREATE (po)-[:Forca]->(gr);

MATCH (voa:Elemento {Tipo:'Voador'}), (gr:Elemento {Tipo:'Grama'})
CREATE (voa)-[:Forca]->(gr);

MATCH (el:Elemento {Tipo:'Eletrico'}), (voa:Elemento {Tipo:'Voador'}), (ag:Elemento {Tipo:'Agua'})
CREATE (el)-[:Forca]->(voa),
       (el)-[:Forca]->(ag);
"""

def execute_query(query):
    with driver.session() as session:
        session.run(query)

execute_query(query)

driver.close()

