#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar páginas HTML de produtos da Fyber Polímeros
"""

# Dados dos produtos organizados por categoria
PRODUTOS = [
    # Fibra de Vidro - JÁ CRIADOS MANUALMENTE
    
    # Equipamentos e Acessórios
    {"nome": "Fita Crepe", "categoria": "Equipamentos e Acessórios", "slug": "fita-crepe", "cat_slug": "equipamentos-acessorios",
     "desc1": "<strong>Fita crepe de alta qualidade</strong> especialmente desenvolvida para uso em processos de laminação e pintura de compósitos. Com adesivo de boa aderência e remoção limpa, é essencial para delimitar áreas, proteger superfícies e criar contornos precisos durante aplicação de gel coats e resinas.",
     "desc2": "Resistente a solventes leves e temperaturas moderadas, a fita crepe profissional oferece <strong>excelente conformabilidade em superfícies curvas</strong> e não deixa resíduos após remoção. Ideal para mascaramento em pintura automotiva, proteção de bordas em laminação e demarcação de áreas em moldes. Disponível em diversas larguras para atender diferentes necessidades.",
     "caract": ["Remoção limpa sem resíduos", "Boa aderência", "Conformável em curvas", "Resistente a solventes leves"]},
    
    {"nome": "Estopas", "categoria": "Equipamentos e Acessórios", "slug": "estopas", "cat_slug": "equipamentos-acessorios",
     "desc1": "<strong>Estopas industriais de algodão</strong> de alta absorção, material indispensável para limpeza de ferramentas, remoção de excessos de resina e manutenção geral em processos de fabricação de compósitos. Produto de ótima qualidade, livre de fiapos e contaminantes.",
     "desc2": "As estopas profissionais são <strong>altamente absorventes e resistentes</strong>, ideais para limpeza com solventes, acetona e produtos químicos utilizados na indústria de fiberglass. Fundamentais para manter ferramentas limpas, remover resíduos de pincéis e rolos, e garantir ambiente de trabalho organizado. Embaladas em fardos para maior economia e praticidade.",
     "caract": ["Alta capacidade de absorção", "Livre de fiapos", "Resistente a solventes", "Ótimo custo-benefício"]},
    
    {"nome": "Máscaras", "categoria": "Equipamentos e Acessórios", "slug": "mascaras", "cat_slug": "equipamentos-acessorios",
     "desc1": "<strong>Máscaras de proteção respiratória profissional</strong> com filtros químicos específicos para vapores orgânicos, essenciais para segurança do trabalhador durante manipulação de resinas, estireno, solventes e produtos químicos utilizados em processos de laminação e acabamento de compósitos.",
     "desc2": "A linha de máscaras oferecidas pela Fyber Polímeros atende às <strong>normas de segurança mais rigorosas</strong>, proporcionando proteção efetiva contra vapores nocivos, poeiras e partículas. Disponíveis em modelos semi-faciais e faciais completos, com cartuchos substituíveis de diferentes especificações. O uso correto de EPIs é fundamental para preservar a saúde respiratória em ambientes industriais. Consulte nossos especialistas para escolher o modelo adequado à sua aplicação.",
     "caract": ["Proteção contra vapores orgânicos", "Filtros substituíveis", "Conformidade com normas de segurança", "Diversos modelos disponíveis"]},
    
    {"nome": "Rolos de Lã", "categoria": "Equipamentos e Acessórios", "slug": "rolos-de-la", "cat_slug": "equipamentos-acessorios",
     "desc1": "<strong>Rolos de lã de carneiro natural</strong> para aplicação de gel coats, pinturas e acabamentos em superfícies de fibra de vidro. Material de alta qualidade que proporciona aplicação uniforme e acabamento profissional sem bolhas ou marcas.",
     "desc2": "Os rolos de lã profissionais são <strong>ideais para aplicação de gel coats</strong> em moldes, garantindo camada homogênea e livre de imperfeições. Disponíveis em diferentes tamanhos e densidades de pelo, adequados para gel coats de diversas viscosidades. Proporcionam excelente acabamento superficial e são facilmente laváveis com acetona para reutilização. Essenciais para obter superfícies lisas e brilhantes em peças de fiberglass.",
     "caract": ["Lã de carneiro natural", "Acabamento profissional", "Diversos tamanhos disponíveis", "Reutilizáveis após limpeza"]},
    
    {"nome": "Pincéis", "categoria": "Equipamentos e Acessórios", "slug": "pinceis", "cat_slug": "equipamentos-acessorios",
     "desc1": "<strong>Pincéis profissionais de cerdas sintéticas</strong> resistentes a solventes, desenvolvidos especificamente para aplicação de resinas, gel coats e agentes desmoldantes. Linha completa de tamanhos e formatos para atender diversas necessidades de laminação e acabamento.",
     "desc2": "Os pincéis da Fyber Polímeros possuem <strong>cerdas de alta qualidade</strong> que não soltam pelos, garantindo aplicação limpa e profissional. Cabos ergonômicos facilitam o manuseio prolongado, enquanto as cerdas sintéticas resistem à ação de estireno e solventes. Ideais para aplicação de gel coat em áreas de difícil acesso, impregnação de fibras e retoques. Disponíveis em diversos tamanhos, de pincéis finos para detalhes até pincéis largos para grandes áreas.",
     "caract": ["Cerdas sintéticas resistentes", "Não soltam pelos", "Cabos ergonômicos", "Linha completa de tamanhos"]},
    
    {"nome": "Lixas", "categoria": "Equipamentos e Acessórios", "slug": "lixas", "cat_slug": "equipamentos-acessorios",
     "desc1": "<strong>Lixas especiais para fibra de vidro</strong> em diversas granulometrias, essenciais para preparação de superfícies, acabamento de laminados e processos de polimento. Grãos de alta qualidade garantem corte eficiente e durabilidade prolongada.",
     "desc2": "A linha de lixas oferecida inclui <strong>grãos de 80 a 2000</strong>, atendendo desde desbaste grosseiro até polimento fino espelhado. Lixas d'água para uso úmido evitam entupimento e proporcionam acabamento superior. Fundamentais para preparar superfícies entre camadas de laminação, remover imperfeições de gel coat e criar acabamento final perfeito. Disponíveis em folhas, discos e rolos para uso manual ou com lixadeiras elétricas.",
     "caract": ["Diversas granulometrias disponíveis", "Lixas d'água e secas", "Alta durabilidade", "Para uso manual ou elétrico"]},
    
    {"nome": "Bucha Celeron", "categoria": "Equipamentos e Acessórios", "slug": "bucha-celeron", "cat_slug": "equipamentos-acessorios",
     "desc1": "<strong>Bucha Celeron de tecido fenólico</strong>, material técnico de alta resistência mecânica e excelente isolamento elétrico. Este compósito de tecido de algodão impregnado com resina fenólica é amplamente utilizado como componente estrutural e isolante em diversas indústrias.",
     "desc2": "A Bucha Celeron oferece <strong>excepcional resistência ao desgaste</strong>, baixo coeficiente de atrito e ótima estabilidade dimensional. Ideal para fabricação de buchas, mancais, engrenagens, isoladores elétricos e componentes de máquinas. Usinável com ferramentas convencionais, permite precisão em tolerâncias apertadas. Disponível em diversos diâmetros e espessuras. Material de longa duração que substitui com vantagens componentes metálicos em muitas aplicações.",
     "caract": ["Alta resistência mecânica", "Baixo coeficiente de atrito", "Isolamento elétrico", "Facilmente usinável"]},
    
    {"nome": "Roletes Fura Bolha", "categoria": "Equipamentos e Acessórios", "slug": "roletes-fura-bolha", "cat_slug": "equipamentos-acessorios",
     "desc1": "<strong>Roletes fura bolha profissionais</strong> com agulhas metálicas, ferramenta essencial para eliminação de bolhas de ar durante laminação de compósitos. Design ergonômico permite trabalho confortável mesmo em laminações extensas.",
     "desc2": "Os roletes fura bolha são <strong>indispensáveis para garantir qualidade</strong> em laminados de fibra de vidro, removendo completamente o ar aprisionado entre camadas de resina e reforço. Disponíveis em diferentes larguras (25mm a 100mm) com agulhas de comprimentos variados para diferentes espessuras de laminação. Rolamento suave facilita o trabalho, enquanto as agulhas perfuram e liberam bolhas sem danificar as fibras. Uso correto garante laminados livres de vazios, com máximas propriedades mecânicas.",
     "caract": ["Eliminação eficiente de bolhas", "Diversos tamanhos disponíveis", "Agulhas de qualidade", "Rolamento suave"]},
    
    {"nome": "Picador Roving", "categoria": "Equipamentos e Acessórios", "slug": "picador-roving", "cat_slug": "equipamentos-acessorios",
     "desc1": "<strong>Picador de roving manual</strong>, ferramenta prática para cortar rovings (mechas de fibra de vidro) em comprimentos controlados, facilitando a preparação de reforços para laminação manual e processos de moldagem.",
     "desc2": "O picador permite <strong>cortes rápidos e precisos</strong> de rovings, agilizando processos de preparação de material. Ideal para criar reforços localizados, adicionar fibras picadas em áreas específicas e preparar cargas de fibra para misturas. Construção robusta em aço, lâminas afiadas e ajuste de comprimento de corte. Ferramenta que aumenta produtividade e padronização em oficinas de laminação.",
     "caract": ["Cortes rápidos e precisos", "Ajuste de comprimento", "Construção robusta", "Aumenta produtividade"]},
    
    # Resinas
    {"nome": "Resinas Éster Vinílicas", "categoria": "Resinas", "slug": "resinas-ester-vinilicas", "cat_slug": "resinas",
     "desc1": "<strong>Resinas Éster Vinílicas de alto desempenho</strong>, combinando as melhores características das resinas epóxi e poliéster. Oferecem resistência química superior, excelentes propriedades mecânicas e ótima processabilidade, sendo a escolha ideal para ambientes agressivos.",
     "desc2": "As Resinas Éster Vinílicas são <strong>especialmente recomendadas para aplicações que exigem resistência química excepcional</strong>, como tanques para produtos químicos, tubulações industriais, equipamentos para tratamento de efluentes e estruturas expostas a ambientes corrosivos. Apresentam excelente resistência a ácidos, álcalis, solventes e condições de alta temperatura. Processo de cura similar ao das resinas poliéster, facilitando a transição para fabricantes. Maior durabilidade e vida útil em aplicações críticas.",
     "caract": ["Superior resistência química", "Excelentes propriedades mecânicas", "Resistência a ambientes agressivos", "Processabilidade facilitada"]},
    
    {"nome": "Resinas Isoftálicas com NPG", "categoria": "Resinas", "slug": "resinas-isoftalicas-npg", "cat_slug": "resinas",
     "desc1": "<strong>Resinas Isoftálicas formuladas com Neopentil Glicol (NPG)</strong>, oferecendo desempenho superior em resistência à hidrólise, melhor estabilidade de cor e propriedades mecânicas aprimoradas. Tecnologia avançada para aplicações náuticas e industriais de alta exigência.",
     "desc2": "O uso de NPG confere às resinas <strong>excelente resistência à degradação por água</strong>, reduzindo significativamente problemas de osmose em aplicações marinhas. Ideais para construção de cascos de embarcações, piscinas, spas e tanques de água. Apresentam cura mais rápida, menor emissão de estireno e melhor resistência UV comparadas às resinas ortoftálicas convencionais. Combinação perfeita de performance técnica e custo-benefício para aplicações profissionais.",
     "caract": ["Resistência superior à hidrólise", "Reduz osmose", "Melhor estabilidade de cor", "Propriedades mecânicas aprimoradas"]},
    
    {"nome": "Resina Isoftálica", "categoria": "Resinas", "slug": "resina-isoftalica", "cat_slug": "resinas",
     "desc1": "<strong>Resina Isoftálica de uso geral</strong>, oferecendo melhor desempenho que resinas ortoftálicas em aplicações que exigem maior resistência química e mecânica. Versátil e confiável para ampla gama de aplicações industriais e náuticas.",
     "desc2": "A Resina Isoftálica apresenta <strong>excelente equilíbrio entre performance e custo</strong>, sendo amplamente utilizada em piscinas, tanques, peças industriais, componentes automotivos e aplicações marinhas. Oferece boa resistência química, propriedades mecânicas superiores e melhor resistência ao intemperismo comparada às resinas ortoftálicas. Facilidade de laminação, tempo de gel controlável e cura confiável. Escolha profissional para projetos que demandam durabilidade e qualidade.",
     "caract": ["Melhor que resinas ortoftálicas", "Boa resistência química", "Versátil", "Ótimo custo-benefício"]},
    
    {"nome": "Resina de Mármores", "categoria": "Resinas", "slug": "resina-de-marmores", "cat_slug": "resinas",
     "desc1": "<strong>Resina específica para mármore sintético</strong>, formulação especial de alta viscosidade e tixotropia controlada, desenvolvida para fabricação de pias, bancadas, tampos e peças decorativas com acabamento tipo mármore ou granito.",
     "desc2": "Esta resina permite a criação de <strong>peças com aparência de pedra natural</strong> através da mistura com cargas minerais, pigmentos e veios coloridos. Oferece excelente trabalhabilidade, baixa retração, dureza superficial adequada para polimento e resistência a produtos de limpeza domésticos. Ideal para indústria de marmoraria sintética, permitindo formas e tamanhos impossíveis com pedras naturais. Cura à temperatura ambiente, dispensando autoclaves. Peças finais com alta qualidade estética e durabilidade.",
     "caract": ["Formulação específica para mármore sintético", "Alta viscosidade e tixotropia", "Excelente polibilidade", "Cura à temperatura ambiente"]},
    
    {"nome": "Resina Ortoftálica", "categoria": "Resinas", "slug": "resina-ortoftalica", "cat_slug": "resinas",
     "desc1": "<strong>Resina Poliéster Ortoftálica de uso geral</strong>, o produto mais versátil e econômico da linha de resinas. Adequada para ampla variedade de aplicações em fibra de vidro, oferecendo bom desempenho mecânico e processabilidade facilitada.",
     "desc2": "A Resina Ortoftálica é a <strong>escolha mais popular para aplicações gerais</strong> como telhas translúcidas, caixas d'água, peças automotivas, móveis, artesanato e reparos diversos. Apresenta boa resistência mecânica, facilidade de laminação, tempo de gel ajustável e cura confiável. Excelente relação custo-benefício para projetos que não exigem resistências químicas ou mecânicas extremas. Compatível com todos os tipos de reforços de fibra de vidro e processos de laminação manual ou spray.",
     "caract": ["Uso geral mais econômico", "Boa resistência mecânica", "Fácil processamento", "Versátil"]},
    
    # Gel Coats
    {"nome": "Gel para Molde", "categoria": "Gel Coats", "slug": "gel-para-molde", "cat_slug": "gel-coats",
     "desc1": "<strong>Gel Coat específico para confecção de moldes</strong>, formulado com maior dureza e resistência à abrasão para suportar múltiplas desmoldagens. Proporciona superfície lisa e resistente que facilita aplicação de desmoldantes e remoção de peças.",
     "desc2": "O Gel para Molde oferece <strong>durabilidade superior em moldes de produção</strong>, mantendo qualidade superficial mesmo após centenas de ciclos. Resistente a produtos químicos de desmoldagem e ao desgaste mecânico constante. Ideal para moldes master de alta produtividade na indústria náutica, automotiva e de componentes em série. Cura com alta dureza superficial, minimiza micro-porosidade e facilita polimento para acabamento espelhado.",
     "caract": ["Alta dureza superficial", "Resistência à abrasão", "Durabilidade em produção", "Facilita desmoldagem"]},
    
    {"nome": "Gel Éster Vinílico", "categoria": "Gel Coats", "slug": "gel-ester-vinilico", "cat_slug": "gel-coats",
     "desc1": "<strong>Gel Coat Éster Vinílico premium</strong>, o mais alto nível de proteção e durabilidade disponível em revestimentos para compósitos. Combina resistência química excepcional com máxima proteção contra osmose e degradação ambiental.",
     "desc2": "O Gel Éster Vinílico é <strong>especificação obrigatória para embarcações de alto padrão</strong> e aplicações críticas em ambientes marinhos e industriais agressivos. Oferece barreira superior contra penetração de água, resistência a produtos químicos severos e estabilidade de cor prolongada mesmo sob exposição solar intensa. Investimento que garante máxima vida útil e mínima manutenção em aplicações expostas a condições extremas. Especialmente recomendado para iates, barcos de competição e tanques químicos.",
     "caract": ["Máxima resistência à osmose", "Superior resistência química", "Proteção premium", "Durabilidade excepcional"]},
    
    {"nome": "Gel Coat Ortoftálico", "categoria": "Gel Coats", "slug": "gel-coat-ortoftalico", "cat_slug": "gel-coats",
     "desc1": "<strong>Gel Coat Ortoftálico econômico</strong> para aplicações gerais que não exigem resistência química ou ambiental extrema. Oferece bom acabamento estético e proteção adequada com excelente relação custo-benefício.",
     "desc2": "O Gel Coat Ortoftálico é <strong>ideal para peças de uso interno</strong>, componentes automotivos, móveis, artigos esportivos e aplicações onde o ambiente não é particularmente agressivo. Proporciona superfície lisa e brilhante, disponível em diversas cores e pode ser pigmentado conforme necessidade. Fácil aplicação, cura confiável e acabamento profissional. Escolha econômica para projetos com orçamento ajustado que não comprometem qualidade visual.",
     "caract": ["Excelente custo-benefício", "Bom acabamento estético", "Fácil aplicação", "Diversas cores disponíveis"]},
    
    # Fibra de Vidro - NOVOS
    {"nome": "Tecido 600g-800g por Metro Quadrado", "categoria": "Fibra de Vidro", "slug": "tecido-600g-800g-por-metro-quadrado", "cat_slug": "fibra-de-vidro",
     "desc1": "<strong>Tecido de fibra de vidro de alta gramatura</strong> (600g/m² a 800g/m²) para aplicações que exigem máxima resistência estrutural. Especialmente desenvolvido para laminação de peças de grande porte, reforços estruturais e aplicações náuticas de alto desempenho.",
     "desc2": "Este tecido de <strong>gramatura pesada</strong> é ideal para construção de cascos de embarcações, tanques industriais, componentes automotivos de alta performance e estruturas que necessitam de excepcional resistência mecânica. Oferece excelente relação resistência/peso, facilidade de laminação e ótima molhabilidade com resinas poliéster e epóxi. Disponível em diferentes padrões de tecelagem para atender necessidades específicas de cada projeto.",
     "caract": ["Alta resistência estrutural", "Gramatura 600g-800g/m²", "Ideal para grandes projetos", "Excelente molhabilidade"]},
    
    # Catalisadores e Aceleradores - NOVOS
    {"nome": "Acelerador Dimetil Anilina", "categoria": "Catalisadores e Aceleradores", "slug": "acelerador-dimetil-anilina", "cat_slug": "catalisadores-aceleradores",
     "desc1": "<strong>Acelerador Dimetil Anilina (DMA)</strong> de alta pureza, essencial para sistemas de cura de resinas epóxi e poliéster em temperatura ambiente. Atua reduzindo o tempo de gel e acelerando o processo de cura sem necessidade de aquecimento.",
     "desc2": "O DMA é <strong>amplamente utilizado em laminação manual</strong> onde se deseja controle preciso do tempo de trabalho e cura rápida. Especialmente eficaz em combinação com peróxidos para sistemas de cura à temperatura ambiente. Dosagem precisa permite ajustar tempo de gel conforme necessidade do processo. Fundamental em oficinas de laminação que buscam produtividade sem comprometer qualidade. Armazenar em local fresco e ao abrigo da luz.",
     "caract": ["Acelera cura em temperatura ambiente", "Alta pureza", "Controle preciso do tempo de gel", "Compatível com diversos sistemas"]},
    
    {"nome": "Catalisador MEK", "categoria": "Catalisadores e Aceleradores", "slug": "catalisador-mek", "cat_slug": "catalisadores-aceleradores",
     "desc1": "<strong>Catalisador MEK (Metil Etil Cetona Peróxido)</strong> de qualidade premium, o catalisador mais utilizado para cura de resinas poliéster e gel coats. Oferece cura rápida, uniforme e confiável em temperatura ambiente.",
     "desc2": "O Catalisador MEK da Fyber Polímeros possui <strong>alta estabilidade e pureza</strong>, garantindo resultados consistentes em processos de laminação. Dosagem típica de 1% a 3% em peso permite ajuste fino do tempo de gel conforme temperatura ambiente e velocidade de trabalho desejada. Embalagem em frascos protegidos da luz UV para máxima durabilidade. Produto essencial em qualquer oficina de fibra de vidro. Seguir sempre as recomendações de segurança do fabricante.",
     "caract": ["Alta pureza e estabilidade", "Cura rápida e uniforme", "Dosagem flexível 1-3%", "Embalagem protegida UV"]},
    
    # Cargas (CATEGORIA NOVA)
    {"nome": "Aerosil-Carbosil", "categoria": "Cargas", "slug": "Aerosil-Carbosil", "cat_slug": "cargas",
     "desc1": "<strong>Aerosil (sílica pirogênica) e Carbosil</strong> de alta qualidade, agentes tixotrópicos essenciais para controle de viscosidade e comportamento reológico de resinas, gel coats e massas de poliéster. Proporcionam propriedades anti-escorrimento e espessamento sem comprometer transparência.",
     "desc2": "Estes produtos são <strong>fundamentais para criar formulações tixotrópicas</strong> que permitem aplicação em superfícies verticais sem escorrimento, essenciais em processos de laminação manual, fabricação de moldes e aplicação de gel coats. Em pequenas dosagens (2-4%), transformam resinas líquidas em géis manejáveis que facilitam o trabalho. Aerosil mantém transparência em sistemas claros, ideal para peças translúcidas. Produto técnico de alto desempenho.",
     "caract": ["Controle de viscosidade", "Propriedades anti-escorrimento", "Mantém transparência", "Baixa dosagem necessária"]},
    
    {"nome": "Alumina Hidratada", "categoria": "Cargas", "slug": "Alumina Hidratada", "cat_slug": "cargas",
     "desc1": "<strong>Alumina Hidratada</strong> (hidróxido de alumínio) de alta pureza, carga mineral retardante de chamas amplamente utilizada em compósitos que exigem propriedades de resistência ao fogo. Material de baixa densidade e excelente trabalhabilidade.",
     "desc2": "A Alumina Hidratada oferece <strong>dupla função: carga econômica e proteção contra fogo</strong>, sendo especificação obrigatória em aplicações náuticas, transporte público, construção civil e indústria eletrônica. Ao ser exposta ao calor, libera água de cristalização, atuando como retardante natural de chamas. Proporciona bom acabamento superficial, reduz retração e melhora estabilidade dimensional. Disponível em diferentes granulometrias para otimizar propriedades específicas de cada aplicação.",
     "caract": ["Retardante de chamas", "Baixa densidade", "Reduz retração", "Excelente trabalhabilidade"]},
    
    {"nome": "Calcita", "categoria": "Cargas", "slug": "Calcita", "cat_slug": "cargas",
     "desc1": "<strong>Calcita</strong> (carbonato de cálcio) micronizada de alta qualidade, carga mineral econômica e versátil para extensão de resinas poliéster. Melhora propriedades mecânicas, reduz custo e facilita lixamento de peças acabadas.",
     "desc2": "A Calcita é a <strong>carga mais utilizada na indústria de compósitos</strong> devido à excelente relação custo-benefício. Aumenta a dureza superficial, melhora resistência à compressão e facilita processos de acabamento. Ideal para fabricação de mármore sintético, massas de poliéster, seladores e cargas. Disponível em diversas granulometrias, desde pós finos para acabamento espelhado até grades grosseiras para enchimento volumétrico. Compatível com todos os tipos de resinas termofixas.",
     "caract": ["Excelente custo-benefício", "Aumenta dureza superficial", "Facilita lixamento", "Versátil"]},
    
    {"nome": "Fibra Moída", "categoria": "Cargas", "slug": "Fibra Moida", "cat_slug": "cargas",
     "desc1": "<strong>Fibra de vidro moída</strong> em comprimentos controlados, excelente reforço tridimensional para massas de poliéster, reparos estruturais e compostos moldáveis (SMC/BMC). Proporciona resistência mecânica superior comparada a cargas minerais convencionais.",
     "desc2": "A Fibra Moída oferece <strong>reforço estrutural efetivo</strong> em aplicações onde não é possível utilizar tecidos ou mantas contínuas. Ideal para formulação de massas de enchimento com alta resistência, reparos estruturais profissionais, preenchimento de núcleos sanduíche e fabricação de peças moldadas. Distribuição uniforme das fibras garante propriedades isotrópicas. Disponível em diferentes comprimentos de corte (3mm, 6mm, 12mm) para otimizar fluidez versus resistência mecânica.",
     "caract": ["Reforço tridimensional", "Alta resistência mecânica", "Diversos comprimentos disponíveis", "Propriedades isotrópicas"]},
    
    {"nome": "Micro Esfera Oca", "categoria": "Cargas", "slug": "Micro Esfera Oca", "cat_slug": "cargas",
     "desc1": "<strong>Micro esferas ocas de vidro</strong>, carga técnica de baixíssima densidade para redução de peso sem sacrifício significativo de propriedades mecânicas. Ideal para aplicações aeronáuticas, náuticas e automotivas de alta performance.",
     "desc2": "As Micro Esferas Ocas são <strong>a solução premium para projetos que exigem máxima leveza</strong>. Com densidade entre 0.15 a 0.60 g/cm³, permitem redução drástica de peso mantendo integridade estrutural. Amplamente utilizadas em ferramentas e moldes de laminação (baixa massa térmica), núcleos sanduíche sintáticos, massas leves de enchimento e aplicações aeroespaciais. Esferas de vidro proporcionam excelente resistência à compressão e estabilidade dimensional. Produto técnico de alto valor agregado.",
     "caract": ["Baixíssima densidade", "Redução drástica de peso", "Resistência à compressão", "Aplicações de alta performance"]},
    
    {"nome": "Talco", "categoria": "Cargas", "slug": "Talco", "cat_slug": "cargas",
     "desc1": "<strong>Talco industrial</strong> micronizado de alta pureza, carga mineral que melhora fluidez, trabalhabilidade e acabamento superficial de resinas e massas de poliéster. Estrutura lamelar proporciona propriedades únicas de processamento.",
     "desc2": "O Talco oferece <strong>excelente lixabilidade e acabamento</strong>, sendo preferido em aplicações automotivas, móveis e peças que exigem pintura posterior. Reduz pegajosidade (tackiness) de resinas, melhora desmoldagem e proporciona superfície mais lisa. Estrutura lamelar atua como barreira contra penetração de umidade. Ideal para massas de acabamento, primers, seladores e formulações que serão pintadas. Disponível em diferentes granulometrias para otimizar brilho e facilidade de lixamento.",
     "caract": ["Excelente lixabilidade", "Melhora acabamento superficial", "Reduz pegajosidade", "Barreira contra umidade"]},
    
    # Desmoldantes (CATEGORIA NOVA)
    {"nome": "Álcool Desmoldante PVA", "categoria": "Desmoldantes", "slug": "alcool Desmoldante PVA", "cat_slug": "demoldantes",
     "desc1": "<strong>Álcool Polivinílico (PVA)</strong> desmoldante solúvel em água, sistema mais utilizado mundialmente para desmoldagem de peças de fibra de vidro. Forma película protetora que garante separação perfeita entre molde e peça laminada.",
     "desc2": "O PVA é <strong>essencial para desmoldagem de laminados</strong> sobre moldes de fibra de vidro. Aplicado antes da laminação, cria barreira entre gel coat do molde e gel coat da peça, permitindo desmoldagem fácil e sem danos. Solúvel em água facilita remoção completa antes de pintura ou colagem. Não contamina superfície, não deixa resíduos oleosos. Sistema econômico e confiável usado em produção industrial e oficinas artesanais. Fundamental em qualquer processo de moldagem por contato.",
     "caract": ["Desmoldagem perfeita", "Solúvel em água", "Não contamina superfície", "Econômico e confiável"]},
    
    {"nome": "Catalisador BPO", "categoria": "Desmoldantes", "slug": "Catalizador BPO", "cat_slug": "demoldantes",
     "desc1": "<strong>Peróxido de Benzoíla (BPO)</strong> em pasta, catalisador de baixa reatividade indicado para cura de resinas em temperatura elevada ou sistemas que exigem tempo de trabalho prolongado. Alternativa ao MEK para aplicações específicas.",
     "desc2": "O BPO é <strong>especialmente indicado para processos em altas temperaturas</strong>, cura em estufa e fabricação de peças por moldagem térmica. Oferece tempo de gel mais longo em temperatura ambiente, permitindo trabalho com grandes volumes de resina. Amplamente utilizado em indústria de botões, peças usinadas e componentes que serão curados em ciclo térmico controlado. Pasta facilita dosagem precisa e homogeneização. Armazenar em local fresco e seco, longe de fontes de calor.",
     "caract": ["Para cura térmica", "Tempo de trabalho prolongado", "Fácil dosagem", "Estável em temperatura ambiente"]},
    
    {"nome": "Cera Desmoldante", "categoria": "Desmoldantes", "slug": "Cera Desmoldante", "cat_slug": "demoldantes",
     "desc1": "<strong>Cera desmoldante profissional</strong> de alta performance, sistema de múltiplas camadas para preparação de moldes e garantia de desmoldagem perfeita. Base para qualquer processo de laminação por contato em moldes novos ou recondicionados.",
     "desc2": "A Cera Desmoldante cria <strong>película protetora de longa duração</strong> que garante múltiplas desmoldagens consecutivas. Aplicação em 3-5 camadas com polimento entre elas sela a porosidade do gel coat do molde e proporciona superfície espelhada. Essencial antes de usar desmoldantes líquidos, forma base durável que protege o molde e facilita limpeza. Produto profissional usado em indústria náutica, automotiva e fabricação de peças em série. Uma boa preparação com cera pode permitir 20-50 desmoldagens antes de reaplicação.",
     "caract": ["Múltiplas desmoldagens", "Proteção duradoura do molde", "Acabamento espelhado", "Base para desmoldantes líquidos"]},
    
    {"nome": "Chemlease 15 Sealer", "categoria": "Desmoldantes", "slug": "Chemlease 15 Sealer", "cat_slug": "demoldantes",
     "desc1": "<strong>Chemlease 15 Sealer</strong>, selador profissional de alta tecnologia da linha Chemlease, líder mundial em sistemas de desmoldagem. Formulação avançada que sela porosidade de moldes novos e prepara superfície para desmoldantes semi-permanentes.",
     "desc2": "Este selador de <strong>nível industrial</strong> é essencial para preparação profissional de moldes novos ou recondicionados. Penetra na microporosidade do gel coat, criando base uniforme e selada que maximiza eficiência de desmoldantes subsequentes. Sistema Chemlease é especificação obrigatória em indústria aeronáutica, automotiva de luxo e fabricação de compósitos de precisão. Uma aplicação correta pode proporcionar centenas de desmoldagens com qualidade consistente. Investimento que se paga rapidamente em produtividade e qualidade superficial.",
     "caract": ["Tecnologia de ponta", "Sela microporosidade", "Maximiza eficiência de desmoldantes", "Padrão industrial internacional"]},
    
    {"nome": "Chemlease MOLD CLEANER Limpador de Moldes", "categoria": "Desmoldantes", "slug": "Chemlease MOLD CLEANER Limpador de Moldes", "cat_slug": "demoldantes",
     "desc1": "<strong>Chemlease Mold Cleaner</strong>, limpador profissional específico para moldes de fibra de vidro e compósitos. Remove resíduos de estireno, acúmulo de desmoldantes, contaminações e prepara superfície para nova aplicação de sistema de desmoldagem.",
     "desc2": "Este limpador foi <strong>especialmente formulado para não danificar gel coat de moldes</strong>, ao contrário de solventes agressivos que podem comprometer a superfície. Remove eficientemente acúmulo de múltiplas camadas de desmoldantes, resíduos de laminação e contaminações diversas. Uso periódico (a cada 30-50 ciclos) mantém molde em condições ideais de produção. Essencial em oficinas profissionais que buscam máxima vida útil dos moldes e qualidade superficial consistente. Produto que garante o investimento em moldes caros.",
     "caract": ["Não danifica gel coat", "Remove resíduos eficientemente", "Uso periódico recomendado", "Prolonga vida útil do molde"]},
    
    # Espumas (CATEGORIA NOVA)
    {"nome": "Espuma de Poliuretano", "categoria": "Espumas", "slug": "Espuma-de-Poliuretano", "cat_slug": "espumas",
     "desc1": "<strong>Espuma de poliuretano rígida</strong> de célula fechada, excelente material de núcleo para estruturas sanduíche em compósitos. Oferece alta resistência ao cisalhamento, baixo peso e facilidade de usinagem para criação de formas complexas.",
     "desc2": "A Espuma de Poliuretano é <strong>amplamente utilizada em construção naval</strong>, pranchas de surf, wind e kitesurf, componentes automotivos e aeronáuticos. Estrutura de célula fechada proporciona flutuabilidade e isolamento térmico. Disponível em diversas densidades (40kg/m³ a 200kg/m³) para otimizar relação resistência/peso conforme aplicação. Facilmente usinável com ferramentas convencionais para criar formas aerodinâmicas ou hidrodinâmicas. Compatível com resinas epóxi e poliéster. Custo-benefício excelente para núcleos estruturais.",
     "caract": ["Célula fechada", "Diversas densidades disponíveis", "Facilmente usinável", "Excelente custo-benefício"]},
    
    # Material de Núcleo - NOVOS
    {"nome": "Coremat", "categoria": "Material de Núcleo", "slug": "Coremat", "cat_slug": "material-de-nucleo",
     "desc1": "<strong>Coremat</strong>, material de núcleo revolucionário composto por fibras não-tecidas que criam estrutura tridimensional. Substitui núcleos rígidos tradicionais em aplicações que exigem conformabilidade em superfícies curvas complexas e aumento de rigidez sem peso excessivo.",
     "desc2": "O Coremat é <strong>ideal para construção naval</strong>, cascos de embarcações, decks, divisórias e painéis estruturais. Estrutura de fibras randomicamente orientadas permite drapeamento perfeito em curvas compostas, impossível com espumas rígidas. Aumenta significativamente a rigidez do laminado (até 3x) com mínimo acréscimo de peso. Processo de laminação convencional, sem necessidade de equipamentos especiais. Absorve resina controladamente, criando gradiente de propriedades da pele externa ao núcleo. Especificação crescente em projetos de engenharia de ponta.",
     "caract": ["Conformável em curvas complexas", "Aumenta rigidez 3x", "Laminação convencional", "Distribuição controlada de resina"]},
    
    {"nome": "Espuma de PET", "categoria": "Material de Núcleo", "slug": "Espuma-de-PET", "cat_slug": "material-de-nucleo",
     "desc1": "<strong>Espuma de PET reciclado</strong> de alta densidade, material de núcleo estrutural sustentável com excelente resistência mecânica. Alternativa ecológica aos núcleos tradicionais, oferecendo propriedades superiores de resistência ao cisalhamento e compressão.",
     "desc2": "A Espuma de PET combina <strong>performance técnica com responsabilidade ambiental</strong>, sendo fabricada 100% de garrafas PET recicladas. Oferece resistência ao cisalhamento superior às espumas de PVC, excelente isolamento térmico e acústico, e resistência a hidrólise e produtos químicos. Ideal para indústria náutica, transporte, construção civil e energia eólica. Disponível em diferentes densidades e espessuras. Facilmente usinável e termoformável. Certificações ambientais facilitam especificação em projetos sustentáveis. Material do futuro em compósitos estruturais.",
     "caract": ["100% reciclável e reciclado", "Resistência superior", "Isolamento térmico e acústico", "Termoformável"]},
    
    {"nome": "Soric", "categoria": "Material de Núcleo", "slug": "Soric", "cat_slug": "material-de-nucleo",
     "desc1": "<strong>Soric</strong>, material de núcleo técnico composto por estrutura tridimensional de tecido espaçado. Oferece excelente drenagem de ar e resina em processos de infusão a vácuo, além de funcionar como núcleo estrutural leve de alta conformabilidade.",
     "desc2": "O Soric é <strong>essencial em processos avançados de infusão</strong> (VARTM, infusão a vácuo), onde atua simultaneamente como meio de distribuição de resina e núcleo estrutural. Estrutura aberta permite fluxo rápido e uniforme de resina, reduzindo tempo de infusão e garantindo molhagem completa. Após cura, funciona como núcleo leve que aumenta rigidez do laminado. Conformabilidade excepcional permite aplicação em geometrias complexas. Reduz peso, aumenta rigidez e acelera produção - tripla vantagem em uma só solução. Especificação crescente em indústria de pás eólicas e aeronáutica.",
     "caract": ["Dupla função: distribuição e núcleo", "Acelera processos de infusão", "Alta conformabilidade", "Aumenta rigidez e reduz peso"]},
    
    # Equipamentos - NOVO
    {"nome": "Pistola Modelo 12", "categoria": "Equipamentos e Acessórios", "slug": "pistola-modelo-12", "cat_slug": "equipamentos-acessorios",
     "desc1": "<strong>Pistola para aplicação por spray Modelo 12</strong>, equipamento profissional para aplicação rápida e uniforme de gel coats, resinas e primers. Atomização de alta qualidade garante acabamento profissional com economia de material.",
     "desc2": "A Pistola Modelo 12 é <strong>ferramenta essencial em oficinas de produção</strong> que buscam produtividade e qualidade. Sistema de atomização pneumática proporciona aplicação uniforme e controlada, reduzindo desperdício de material caro como gel coats. Ideal para aplicação em moldes de grande porte, produção em série e projetos que exigem rapidez. Fácil limpeza e manutenção, regulagem de vazão e padrão de spray. Construção robusta em materiais resistentes a solventes. Investimento que se paga rapidamente em ganho de produtividade e redução de retrabalho.",
     "caract": ["Aplicação profissional por spray", "Atomização de alta qualidade", "Economia de material", "Fácil limpeza e manutenção"]},
    
    # Continua com outras categorias...
]

# Template HTML base
def gerar_html(produto):
    template = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{produto['nome']} - Fyber Polímeros. {produto['desc1'][:100]}">
  <title>{produto['nome']} - Fyber Polímeros</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css?v=2.0">
  <link rel="icon" type="image/svg+xml" href="../assets/logo_fiber-polimeros-menu.svg">
  <style>
    /* Animação de entrada da página */
    @keyframes fadeInUp {{
      from {{
        opacity: 0;
        transform: translateY(30px);
      }}
      to {{
        opacity: 1;
        transform: translateY(0);
      }}
    }}
    
    .animate-in {{
      animation: fadeInUp 0.6s ease-out forwards;
    }}
    
    /* Estilos para galeria de imagens do produto */
    .produto-galeria {{
      position: relative;
      width: 100%;
    }}
    
    .produto-imagem-principal {{
      width: 100%;
      height: 500px;
      object-fit: cover;
      border-radius: 16px;
      background: linear-gradient(135deg, #0200d2 0%, #0100b8 100%);
      cursor: pointer;
      transition: transform 0.3s ease;
      display: block;
    }}
    
    .produto-imagem-principal:hover {{
      transform: scale(1.02);
    }}
    
    .produto-miniaturas {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
      gap: 0.75rem;
      margin-top: 1rem;
    }}
    
    .produto-miniatura {{
      width: 100%;
      height: 80px;
      object-fit: cover;
      border-radius: 8px;
      cursor: pointer;
      border: 3px solid transparent;
      transition: all 0.3s ease;
    }}
    
    .produto-miniatura:hover {{
      border-color: var(--azul-escuro);
      transform: scale(1.05);
    }}
    
    .produto-miniatura.ativa {{
      border-color: var(--azul-escuro);
    }}
    
    /* Modal para visualização em tela cheia */
    .modal-galeria {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.95);
      z-index: 10000;
      align-items: center;
      justify-content: center;
    }}
    
    .modal-galeria.ativo {{
      display: flex;
    }}
    
    .modal-conteudo {{
      position: relative;
      max-width: 90%;
      max-height: 90%;
    }}
    
    .modal-imagem {{
      max-width: 100%;
      max-height: 90vh;
      object-fit: contain;
      border-radius: 8px;
    }}
    
    .modal-fechar {{
      position: absolute;
      top: -40px;
      right: 0;
      color: white;
      font-size: 2rem;
      cursor: pointer;
      background: none;
      border: none;
      padding: 0.5rem 1rem;
    }}
    
    .modal-navegacao {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(255, 255, 255, 0.2);
      color: white;
      border: none;
      font-size: 2rem;
      padding: 1rem;
      cursor: pointer;
      border-radius: 50%;
      transition: background 0.3s ease;
    }}
    
    .modal-navegacao:hover {{
      background: rgba(255, 255, 255, 0.4);
    }}
    
    .modal-anterior {{
      left: -60px;
    }}
    
    .modal-proximo {{
      right: -60px;
    }}
    
    @media (max-width: 768px) {{
      .produto-imagem-principal {{
        height: 300px;
      }}
      
      .produto-miniaturas {{
        grid-template-columns: repeat(auto-fill, minmax(60px, 1fr));
        gap: 0.5rem;
      }}
      
      .produto-miniatura {{
        height: 60px;
      }}
      
      .modal-navegacao {{
        font-size: 1.5rem;
        padding: 0.5rem;
      }}
      
      .modal-anterior {{
        left: 10px;
      }}
      
      .modal-proximo {{
        right: 10px;
      }}
    }}
  </style>
</head>
<body>
  <div class="mini-banner"><p>Entregamos para todo o Brasil</p></div>
  <header>
    <div class="header-container">
      <a href="../index.html" class="logo"><img src="../assets/logo_fiber-polimeros-menu.svg" alt="Fyber Polímeros" class="logo-img"></a>
      <button class="menu-toggle" aria-label="Menu">☰</button>
      <nav>
        <ul>
          <li><a href="../index.html">Home</a></li>
          <li><a href="../produtos.html">Produtos</a></li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle">Categorias<span class="chevron">▼</span></a>
            <ul class="dropdown-menu">
              <li><a href="../produtos.html#fibra-de-vidro">Fibra de Vidro</a></li>
              <li><a href="../produtos.html#equipamentos-acessorios">Equipamentos e Acessórios</a></li>
              <li><a href="../produtos.html#resinas">Resinas</a></li>
              <li><a href="../produtos.html#gel-coats">Gel Coats</a></li>
              <li><a href="../produtos.html#desmoldantes">Desmoldantes</a></li>
              <li><a href="../produtos.html#cargas">Cargas</a></li>
              <li><a href="../produtos.html#material-de-nucleo">Material de Núcleo</a></li>
              <li><a href="../produtos.html#pigmentos">Pigmentos</a></li>
              <li><a href="../produtos.html#catalisadores-aceleradores">Catalisadores e Aceleradores</a></li>
              <li><a href="../produtos.html#silicones">Silicones</a></li>
              <li><a href="../produtos.html#espumas">Espumas</a></li>
            </ul>
          </li>
          <li><a href="../quem-somos.html">Quem Somos</a></li>
          <li><a href="../contato.html">Contato</a></li>
        </ul>
      </nav>
    </div>
  </header>
  
  <!-- Loader -->
  <div id="pageLoader" style="position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: rgba(255,255,255,0.98); backdrop-filter: blur(10px); z-index: 99999; display: flex; align-items: center; justify-content: center;">
    <div style="text-align: center;">
      <div style="width: 60px; height: 60px; border: 6px solid #f3f3f3; border-top: 6px solid #0200d2; border-radius: 50%; animation: spinLoader 0.8s linear infinite; margin: 0 auto 1.5rem; box-shadow: 0 4px 12px rgba(2,0,210,0.2);"></div>
      <p style="color: #0200d2; font-weight: 700; font-size: 1.1rem; letter-spacing: 0.5px;">Carregando...</p>
    </div>
  </div>
  <style>
    @keyframes spinLoader {{
      0% {{ transform: rotate(0deg); }}
      100% {{ transform: rotate(360deg); }}
    }}
    body.loading {{
      overflow: hidden;
    }}
  </style>
  
  <main style="padding-top: 140px; min-height: 100vh;">
    <div class="animate-in">
      <section style="padding: 2rem 2rem 0; max-width: 1400px; margin: 0 auto;">
        <p style="color: #6B7280; font-size: 0.875rem;">
          <a href="../index.html" style="color: var(--azul-escuro);">Home</a> > 
          <a href="../produtos.html#{produto['cat_slug']}" style="color: var(--azul-escuro);">{produto['categoria']}</a> > 
          <strong>{produto['nome']}</strong>
        </p>
      </section>
      <section style="padding: 2rem;">
        <div style="max-width: 1400px; margin: 0 auto;">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: start;">
            <div class="produto-galeria">
            <img id="imagemPrincipal" 
                 src="../assets/img/produtos/{produto['cat_slug']}/{produto['slug']}/1.webp" 
                 alt="{produto['nome']}" 
                 class="produto-imagem-principal"
                 onclick="abrirModal(0)"
                 onerror="carregarImagemPadrao(this, '{produto['nome']}')">
            <div id="miniaturas" class="produto-miniaturas"></div>
          </div>
          <div>
            <h1 style="color: var(--azul-escuro); margin-bottom: 1.5rem;">{produto['nome']}</h1>
            <div style="margin-bottom: 2rem; line-height: 1.8;">
              <p>{produto['desc1']}</p>
              <p>{produto['desc2']}</p>
            </div>
            <div style="background-color: var(--cinza-claro); padding: 2rem; border-radius: 16px; margin-bottom: 2rem;">
              <h3 style="color: var(--azul-escuro); margin-bottom: 1rem;">Características Principais</h3>
              <ul style="list-style: none; padding: 0;">
'''
    
    for caract in produto['caract']:
        template += f'''                <li style="padding: 0.5rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: var(--azul-escuro); font-weight: bold;">✓</span>{caract}</li>
'''
    
    template += f'''              </ul>
            </div>
            <a href="https://wa.me/557191049971?text=Olá,%20gostaria%20de%20fazer%20um%20orçamento%20para%20{produto['nome'].replace(' ', '%20')}" 
               class="btn btn-primary btn-whatsapp" 
               target="_blank" 
               rel="noopener noreferrer" 
               style="width: 100%; justify-content: center; background-color: #2563eb; padding: 1rem 2rem; font-size: 1.1rem; font-weight: 600;">
              Fazer orçamento
            </a>
          </div>
        </div>
      </div>
    </section>
    </div>
  </main>
  
  <!-- Modal para visualização em tela cheia -->
  <div id="modalGaleria" class="modal-galeria" onclick="fecharModal(event)">
    <div class="modal-conteudo">
      <button class="modal-fechar" onclick="fecharModal(event)">×</button>
      <button class="modal-navegacao modal-anterior" onclick="navegarModal(-1, event)">‹</button>
      <img id="modalImagem" class="modal-imagem" src="" alt="">
      <button class="modal-navegacao modal-proximo" onclick="navegarModal(1, event)">›</button>
    </div>
  </div>
  
  <footer>
    <div class="footer-content">
      <p>2026 — Todos os direitos reservados — Fyber Polímeros.</p>
      <p>Este site tem como objetivo garantir a melhor experiência possível para o usuário.</p>
    </div>
  </footer>
  
  <script src="../script.js"></script>
  <script>
    // Sistema de galeria de imagens do produto
    const imagensDisponiveis = [];
    let indiceAtual = 0;
    const caminhoBase = '../assets/img/produtos/{produto['cat_slug']}/{produto['slug']}/';
    
    // Função para carregar imagem padrão se não houver imagens
    function carregarImagemPadrao(img, nomeProduto) {{
      img.style.display = 'flex';
      img.style.alignItems = 'center';
      img.style.justifyContent = 'center';
      img.innerHTML = '<div style="color: white; font-size: 2rem; font-weight: 700; text-align: center;">' + nomeProduto + '</div>';
      img.onclick = null;
    }}
    
    // Tentar carregar múltiplas imagens
    function carregarImagens() {{
      const extensoes = ['jpg', 'jpeg', 'png', 'webp'];
      const maxImagens = 10; // Tentar até 10 imagens
      let promises = [];
      
      for (let i = 1; i <= maxImagens; i++) {{
        for (let ext of extensoes) {{
          promises.push(
            verificarImagem(caminhoBase + i + '.' + ext)
              .then(url => {{
                if (url && !imagensDisponiveis.includes(url)) {{
                  imagensDisponiveis.push(url);
                }}
              }})
              .catch(() => {{}})
          );
        }}
      }}
      
      Promise.all(promises).then(() => {{
        if (imagensDisponiveis.length > 0) {{
          // Ordenar imagens
          imagensDisponiveis.sort();
          
          // Definir primeira imagem
          document.getElementById('imagemPrincipal').src = imagensDisponiveis[0];
          document.getElementById('imagemPrincipal').onerror = null;
          
          // Criar miniaturas se houver mais de uma imagem
          if (imagensDisponiveis.length > 1) {{
            criarMiniaturas();
          }}
        }}
      }});
    }}
    
    // Verificar se uma imagem existe
    function verificarImagem(url) {{
      return new Promise((resolve, reject) => {{
        const img = new Image();
        img.onload = () => resolve(url);
        img.onerror = reject;
        img.src = url;
      }});
    }}
    
    // Criar miniaturas
    function criarMiniaturas() {{
      const container = document.getElementById('miniaturas');
      container.innerHTML = '';
      
      imagensDisponiveis.forEach((url, index) => {{
        const img = document.createElement('img');
        img.src = url;
        img.alt = 'Miniatura ' + (index + 1);
        img.className = 'produto-miniatura' + (index === 0 ? ' ativa' : '');
        img.onclick = () => trocarImagem(index);
        container.appendChild(img);
      }});
    }}
    
    // Trocar imagem principal
    function trocarImagem(index) {{
      indiceAtual = index;
      document.getElementById('imagemPrincipal').src = imagensDisponiveis[index];
      
      // Atualizar classe ativa nas miniaturas
      const miniaturas = document.querySelectorAll('.produto-miniatura');
      miniaturas.forEach((mini, i) => {{
        mini.classList.toggle('ativa', i === index);
      }});
    }}
    
    // Abrir modal
    function abrirModal(index) {{
      if (imagensDisponiveis.length === 0) return;
      
      indiceAtual = index;
      document.getElementById('modalImagem').src = imagensDisponiveis[index];
      document.getElementById('modalGaleria').classList.add('ativo');
      document.body.style.overflow = 'hidden';
    }}
    
    // Fechar modal
    function fecharModal(event) {{
      if (event.target.id === 'modalGaleria' || event.target.classList.contains('modal-fechar')) {{
        event.stopPropagation();
        document.getElementById('modalGaleria').classList.remove('ativo');
        document.body.style.overflow = '';
      }}
    }}
    
    // Navegar no modal
    function navegarModal(direcao, event) {{
      event.stopPropagation();
      indiceAtual = (indiceAtual + direcao + imagensDisponiveis.length) % imagensDisponiveis.length;
      document.getElementById('modalImagem').src = imagensDisponiveis[indiceAtual];
      trocarImagem(indiceAtual);
    }}
    
    // Teclas de navegação
    document.addEventListener('keydown', (e) => {{
      const modal = document.getElementById('modalGaleria');
      if (modal.classList.contains('ativo')) {{
        if (e.key === 'Escape') {{
          fecharModal({{ target: modal }});
        }} else if (e.key === 'ArrowLeft') {{
          navegarModal(-1, {{ stopPropagation: () => {{}} }});
        }} else if (e.key === 'ArrowRight') {{
          navegarModal(1, {{ stopPropagation: () => {{}} }});
        }}
      }}
    }});
    
    // Adicionar classe loading ao body
    document.body.classList.add('loading');
    
    // Carregar imagens ao carregar a página
    window.addEventListener('load', carregarImagens);
    
    // Esconder loader quando página carregar
    window.addEventListener('load', function() {{
      setTimeout(function() {{
        const loader = document.getElementById('pageLoader');
        if (loader) {{
          loader.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
          loader.style.opacity = '0';
          loader.style.transform = 'scale(0.95)';
          document.body.classList.remove('loading');
          setTimeout(function() {{
            loader.style.display = 'none';
          }}, 500);
        }}
      }}, 200);
    }});
  </script>
</body>
</html>
'''
    return template

# Gerar arquivos HTML
if __name__ == "__main__":
    import os
    import sys
    
    # Criar diretório produtos se não existir
    os.makedirs("produtos", exist_ok=True)
    
    # Verificar se deve criar pastas de imagens
    criar_pastas = '--criar-pastas' in sys.argv or '-p' in sys.argv
    
    if criar_pastas:
        print("\n📁 Criando estrutura de pastas para imagens...")
        for produto in PRODUTOS:
            pasta_imagens = f"assets/img/produtos/{produto['cat_slug']}/{produto['slug']}"
            os.makedirs(pasta_imagens, exist_ok=True)
            print(f"  ✓ {pasta_imagens}")
        print(f"\n✓ {len(PRODUTOS)} pastas de imagens criadas!")
    
    # Gerar páginas HTML
    print("\n📄 Gerando páginas HTML...")
    for produto in PRODUTOS:
        filename = f"produtos/{produto['slug']}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(gerar_html(produto))
        print(f"  ✓ {filename}")
    
    print(f"\n✅ Total: {len(PRODUTOS)} páginas criadas com sucesso!")
    print("\n" + "="*60)
    print("INSTRUÇÕES PARA ADICIONAR IMAGENS:")
    print("="*60)
    print("1. Coloque as imagens dos produtos nas pastas:")
    print("   assets/img/produtos/[categoria]/[produto]/")
    print("\n2. Nomeie as imagens como:")
    print("   - 1.jpg, 2.jpg, 3.jpg, etc.")
    print("   - Ou use nomes descritivos: frente.jpg, lado.jpg, etc.")
    print("\n3. Formatos suportados: .jpg, .jpeg, .png, .webp")
    print("\n4. A primeira imagem será a imagem principal")
    print("   As demais aparecerão na galeria")
    print("="*60)



