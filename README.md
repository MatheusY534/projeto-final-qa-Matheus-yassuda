# projeto-final-qa-Matheus-yassuda

Teste_01.py
https://colab.research.google.com/drive/1aetQ0h3KuwlUSDVFE1sVOG68q_EwUPcN

Teste_02.py
https://colab.research.google.com/drive/1QESzZvsPggblXSpm_6oDS8DSCM1BdjKG

Teste_03.py
https://colab.research.google.com/drive/1RWdMYt9G97wn-fFDB8S6NY5tp5e0idYO


# 📊 Atividade de Quality Assurance (QA)

1. Apresentação
   
Nome completo: Matheus Chinen Yassuda
Curso e semestre: Quality Assurance - 5º Semestre  

 
Durante este semestre, tive contato com os conceitos de Quality Assurance, onde pude entender na prática como os testes são fundamentais para garantir a qualidade do software. Aprendi a planejar, executar e automatizar testes, além de integrá-los em pipelines de CI/CD.



2. O que é Quality Assurance (QA)?
   
QA é um conjunto de processos e práticas que garantem que um software atenda aos requisitos de qualidade antes de chegar ao usuário.



3. Conceitos Aprendidos Durante o Semestre

Neste semestre, os conceitos que foram que:
Qualidade em software refere-se ao conjunto de características que tornam um produto de software adequado ao seu propósito, atendendo às necessidades dos usuários e stakeholders, já a cultura de qualidade é um ambiente em que todos na equipe priorizam a qualidade desde o início do projeto, não apenas como uma etapa final de testes.
Os testes de QA servem para garantir a qualidade do software, assegurando que ele atenda aos requisitos funcionais, não-funcionais e às expectativas dos usuários.
O planejamentos de testes garente que os esforços de teste sejam eficientes, organizados e alinhados com os objetivos do projeto.
O Google colab serve para escrever, executar e compartilhar código Python diretamente no navegador, sem necessidade de configuração local, já o GitHub serve armazenar, gerenciar, colaborar e distribuir software.
A automação de testes é o uso de scripts e ferramentas para executar testes de software automaticamente, sem intervenção manual e o CI/CD serve para integrar código frequentemente em um repositório compartilhado, onde testes automatizados são executados a cada alteração.
O monitoramento e controle de qualidade em software são processos contínuos que garantem que um produto de software mantenha padrões de qualidade durante e após o desenvolvimento, identificando e corrigindo problemas antes que afetem os usuários finais.



4. Ferramentas e Sites Utilizados

- https://colab.research.google.com
- https://github.com 



 5. Explicação dos Testes Entregues
    
✅ Teste 01 – Teste de Automação Selenium

Biblioteca: selenium
Objetivo: test_login: Verificar se o usuário consegue fazer login com credenciais válidas.
          test_add_to_cart: Validar se um produto pode ser adicionado ao carrinho.
          test_checkout_process: Testar o fluxo completo de checkout (carrinho, informações de envio e confirmação).
    
Resultado esperado: test_login: O URL deve mudar para inventory.html após o login.
                    test_add_to_cart:O ícone do carrinho deve exibir "1" (quantidade de itens adicionados)
                    test_checkout_process:A mensagem "Thank you for your order!" deve aparecer na confirmação final.

Arquivo: https://colab.research.google.com/drive/1aetQ0h3KuwlUSDVFE1sVOG68q_EwUPcN

 ✅ Teste 02 –  Teste Unitário
 
Biblioteca: unittest
Objetivo: Verificar se a função soma(a, b) comporta-se corretamente em diferentes cenários:

test_soma_positivos: Validar soma de números positivos.
test_soma_negativos: Validar soma de números negativos.
test_soma_mista: Validar soma entre positivo e negativo.
test_soma_zero: Validar soma quando um ou ambos os valores são zero.

Resultado esperado:  
test_soma_positivos	soma(2, 3)	5
test_soma_negativos	soma(-1, -1)	-2
test_soma_mista	soma(5, -3)	2
test_soma_zero	soma(0, 0)	0

Arquivo: https://colab.research.google.com/drive/1QESzZvsPggblXSpm_6oDS8DSCM1BdjKG

 ✅ Teste 03 – Teste WSC 
 
Biblioteca: transformers, torch
Objetivo: Avaliar a capacidade de um modelo de linguagem em resolver problemas de desambiguação referencial
Resultado esperado: Identificar corretamente a referência ambígua no contexto
Arquivo: https://colab.research.google.com/drive/1RWdMYt9G97wn-fFDB8S6NY5tp5e0idYO


6. Conclusão Final  
O mais importante que aprendi foi como os testes automatizados podem ser poderosos para escalar a qualidade do software. Enxergo QA como uma área essencial no meu futuro profissional, especialmente com a crescente demanda por DevOps e automação. A ferramenta que mais me chamou atenção foi o GitHub, por causa da grande utilização pelo mercado e por permitir integrar testes diretamente no fluxo de desenvolvimento, tornando o processo ágil e confiável.  
