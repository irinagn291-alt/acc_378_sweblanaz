from pathlib import Path
import json
p=Path(__file__).resolve().parents[1]/'DessertBook/Resources'
langs=['en','de','fr','pt-BR']
rows='''app.name|Dessert Book|Dessert Book|Dessert Book|Dessert Book
recipes|Recipes|Rezepte|Recettes|Receitas
shopping|Shopping list|Einkaufsliste|Liste de courses|Lista de compras
planner|Baking plan|Backplan|Programme|Planejamento
favorites|Favorites|Favoriten|Favoris|Favoritos
settings|Preferences|Einstellungen|Préférences|Preferências
notice|Dessert Book|Dessert Book|Dessert Book|Dessert Book
ok|OK|OK|OK|OK
home.eyebrow|A little homemade happiness|Kleine Glücksmomente|Le bonheur fait maison|Felicidade feita em casa
home.title|Something sweet,\nmade by you.|Etwas Süßes,\nvon dir gemacht.|Une douceur,\nfaite par vous.|Um doce,\nfeito por você.
home.sub|Find your next favorite bake.|Entdecke dein nächstes Lieblingsrezept.|Trouvez votre prochaine recette préférée.|Encontre sua próxima receita favorita.
daily|Recipe of the day|Rezept des Tages|Recette du jour|Receita do dia
open.recipe|Open the recipe|Rezept öffnen|Voir la recette|Ver a receita
all|All recipes|Alle Rezepte|Toutes les recettes|Todas
seasonal|In season|Saisonal|De saison|Da estação
cake|Cakes|Kuchen|Gâteaux|Bolos
quick|Everyday treats|Für jeden Tag|Douceurs du quotidien|Doces do dia a dia
nobake|No bake|Ohne Backen|Sans cuisson|Sem forno
collection|The recipe shelf|Das Rezeptregal|Le carnet de recettes|O caderno de receitas
ingredients|Ingredients|Zutaten|Ingrédients|Ingredientes
filter.active|Products selected|Zutaten gewählt|Ingrédients choisis|Ingredientes selecionados
clear.filters|Clear filters|Filter zurücksetzen|Effacer les filtres|Limpar filtros
empty.search|No recipe found|Kein Rezept gefunden|Aucune recette trouvée|Nenhuma receita encontrada
empty.search.sub|Try fewer ingredients or a different search.|Wähle weniger Zutaten oder einen anderen Suchbegriff.|Essayez moins d’ingrédients ou une autre recherche.|Tente menos ingredientes ou outra busca.
offline.caption|Always in your kitchen. All recipes work offline.|Immer in deiner Küche. Alle Rezepte funktionieren offline.|Toujours en cuisine. Toutes les recettes sont hors ligne.|Sempre na sua cozinha. Todas as receitas funcionam offline.
search|Search recipes or ingredients|Rezepte oder Zutaten suchen|Recettes ou ingrédients|Buscar receitas ou ingredientes
pantry.help|Show recipes that include every selected ingredient. Other ingredients may still be needed.|Zeige Rezepte mit allen gewählten Zutaten. Weitere Zutaten können nötig sein.|Affiche les recettes contenant tous les ingrédients choisis. D’autres ingrédients peuvent être nécessaires.|Mostra receitas com todos os ingredientes escolhidos. Outros ingredientes podem ser necessários.
reset|Reset|Zurücksetzen|Réinitialiser|Redefinir
done|Done|Fertig|Terminé|Concluir
min|min|Min.|min|min
servings|portions|Portionen|portions|porções
resume.cooking|Continue cooking|Weiterbacken|Reprendre la préparation|Continuar o preparo
start.cooking|Let’s bake|Losbacken|C’est parti|Vamos preparar
plan.recipe|Plan this recipe|Rezept einplanen|Programmer cette recette|Planejar receita
timer|Oven timer|Backtimer|Minuteur|Temporizador
scaling.note|Ingredient amounts are scaled. Round eggs sensibly; pan size and cooking time may need adjusting.|Zutaten sind umgerechnet. Eier sinnvoll runden; Formgröße und Backzeit eventuell anpassen.|Les quantités sont ajustées. Arrondissez les œufs ; adaptez le moule et la cuisson si nécessaire.|Quantidades ajustadas. Arredonde os ovos com cuidado; a forma e o tempo podem precisar de ajuste.
add.shopping|Add to shopping list|Zur Einkaufsliste|Ajouter aux courses|Adicionar às compras
update.shopping|Update shopping list|Einkaufsliste aktualisieren|Actualiser les courses|Atualizar compras
allergens|Allergens:|Allergene:|Allergènes :|Alérgenos:
method|The method|Zubereitung|La préparation|Modo de preparo
my.notes|Your kitchen notes|Deine Küchennotizen|Vos notes de cuisine|Suas anotações
notes.placeholder|What would you try next time?|Was möchtest du nächstes Mal ändern?|Que changer la prochaine fois ?|O que você mudaria na próxima vez?
photo.caption|Serving images are AI-created illustrations. Results vary with ingredients and equipment.|Servierbilder sind KI-generierte Illustrationen. Ergebnisse hängen von Zutaten und Geräten ab.|Les images sont des illustrations générées par IA. Le résultat dépend des ingrédients et du matériel.|Imagens ilustrativas criadas por IA. O resultado varia com ingredientes e equipamentos.
favorite|Save as favorite|Als Favorit speichern|Ajouter aux favoris|Salvar nos favoritos
unfavorite|Remove from favorites|Aus Favoriten entfernen|Retirer des favoris|Remover dos favoritos
step|Step|Schritt|Étape|Etapa
start.timer|Start timer|Timer starten|Lancer le minuteur|Iniciar temporizador
back|Back|Zurück|Retour|Voltar
finish|Finish recipe|Rezept abschließen|Terminer la recette|Concluir receita
next|Next step|Nächster Schritt|Étape suivante|Próxima etapa
cooking.complete|Made with a little love.|Mit Liebe gemacht.|Préparé avec amour.|Feito com carinho.
cooking.complete.sub|Your recipe is complete. Save a note about how it went.|Dein Rezept ist fertig. Halte deine Erfahrung in einer Notiz fest.|La recette est terminée. Notez vos impressions.|Receita concluída. Anote como ficou.
restart|Start again|Neu beginnen|Recommencer|Recomeçar
cooking.save|Your place is saved automatically, even when you close the app.|Dein Fortschritt wird auch beim Schließen automatisch gespeichert.|Votre progression est enregistrée même si vous fermez l’app.|Seu progresso é salvo mesmo ao fechar o app.
cooking|Step by step|Schritt für Schritt|Pas à pas|Passo a passo
close|Close|Schließen|Fermer|Fechar
timer.notify|Notify me when ready|Bei Ablauf benachrichtigen|Me prévenir à la fin|Avisar quando terminar
timer.explain|If you enable this, iOS asks to send a local alert. The timer works without notification permission.|Wenn aktiviert, fragt iOS nach lokalen Mitteilungen. Der Timer läuft auch ohne Erlaubnis.|Si activé, iOS demande l’autorisation d’une alerte locale. Le minuteur fonctionne sans cette autorisation.|Ao ativar, o iOS pede permissão para um aviso local. O temporizador funciona sem essa permissão.
timer.safety|A kitchen aid, not a safety alarm. Check your oven and food regularly. Only one timer can run at a time.|Eine Küchenhilfe, kein Sicherheitsalarm. Ofen und Speisen regelmäßig prüfen. Ein Timer gleichzeitig.|Une aide en cuisine. Surveillez régulièrement le four et les aliments. Un seul minuteur à la fois.|Uma ajuda na cozinha. Confira o forno e os alimentos regularmente. Um temporizador por vez.
ready|Your bake is ready to check|Zeit, die Backware zu prüfen|Vérifiez votre préparation|Hora de conferir o preparo
paused|Paused|Pausiert|En pause|Pausado
oven|In the oven|Im Ofen|Au four|No forno
pause|Pause|Pausieren|Pause|Pausar
resume|Resume|Fortsetzen|Reprendre|Retomar
cancel.timer|Cancel timer|Timer beenden|Annuler le minuteur|Cancelar temporizador
shopping.eyebrow|A thoughtful little list|Gut vorbereitet|Une liste bien pensée|Uma lista com carinho
shopping.title|Ready for the pantry.|Alles für den Vorrat.|Pour votre placard.|Tudo para a despensa.
shopping.sub|Shared ingredients, neatly added together.|Gleiche Zutaten werden zusammengezählt.|Les ingrédients communs sont additionnés.|Ingredientes em comum somados.
shopping.empty|Your basket is waiting|Dein Korb wartet|Votre panier vous attend|Sua cesta está esperando
shopping.empty.sub|Open a recipe and add its ingredients here.|Öffne ein Rezept und füge seine Zutaten hinzu.|Ouvrez une recette pour ajouter ses ingrédients.|Abra uma receita e adicione os ingredientes aqui.
checked|checked off|abgehakt|cochés|marcados
selected.recipes|On your menu|Auf deinem Menü|À votre menu|No seu cardápio
remove|Remove|Entfernen|Supprimer|Remover
share.list|Share the list|Liste teilen|Partager la liste|Compartilhar lista
clear.list|Clear list|Liste leeren|Vider la liste|Limpar lista
clear.confirm|Remove all recipes from the shopping list?|Alle Rezepte aus der Einkaufsliste entfernen?|Retirer toutes les recettes de la liste ?|Remover todas as receitas da lista de compras?
bake.date|Date and time|Datum und Uhrzeit|Date et heure|Data e hora
plan.help|The plan is saved on this device. You can optionally send an entry to Apple Reminders from the plan screen.|Der Plan wird lokal gespeichert. Einträge kannst du im Backplan optional an Apple Erinnerungen senden.|Le programme est enregistré ici. Vous pouvez exporter une entrée vers Rappels depuis le programme.|O plano é salvo no aparelho. Você pode exportar um item para Lembretes na tela de planejamento.
save.plan|Save to plan|Im Plan speichern|Enregistrer|Salvar no plano
cancel|Cancel|Abbrechen|Annuler|Cancelar
planner.eyebrow|Make room for good things|Zeit für schöne Dinge|Du temps pour les douceurs|Tempo para coisas boas
planner.title|A week worth baking.|Eine Woche voller Genuss.|Une semaine gourmande.|Uma semana mais doce.
planner.sub|Plan a few bakes, one lovely day at a time.|Plane deine Backideen Tag für Tag.|Programmez vos recettes au fil des jours.|Planeje seus preparos, um dia de cada vez.
plan.add|Add a recipe|Rezept hinzufügen|Ajouter une recette|Adicionar receita
plan.empty|A fresh page for your week|Eine neue Seite für die Woche|Une nouvelle page pour la semaine|Uma página nova para a semana
plan.empty.sub|Choose a recipe and a time to make it.|Wähle ein Rezept und einen Zeitpunkt.|Choisissez une recette et une date.|Escolha uma receita e um horário.
reminder.export|Send to Reminders|An Erinnerungen senden|Envoyer vers Rappels|Enviar para Lembretes
reminder.update|Update reminder|Erinnerung aktualisieren|Actualiser le rappel|Atualizar lembrete
plan.cart|Add next 7 days to shopping|Nächste 7 Tage zur Einkaufsliste|Ajouter les 7 prochains jours aux courses|Adicionar próximos 7 dias às compras
plan.cart.done|Planned portions were added to your shopping list.|Geplante Portionen wurden zur Einkaufsliste addiert.|Les portions prévues ont été ajoutées aux courses.|As porções planejadas foram adicionadas à lista.
plan.reminder.help|Reminders are optional. Removing a plan here keeps any reminder you exported in Apple Reminders.|Erinnerungen sind optional. Exportierte Erinnerungen bleiben beim Löschen eines Planeintrags in Apple Erinnerungen.|Les rappels sont facultatifs. Supprimer une entrée ici conserve le rappel exporté dans Rappels.|Os lembretes são opcionais. Remover um plano aqui mantém o lembrete exportado no app Lembretes.
choose.recipe|Choose a recipe|Rezept wählen|Choisir une recette|Escolher receita
favorites.eyebrow|Keep the good ones close|Die Liebsten immer dabei|Gardez vos préférées|Suas preferidas por perto
favorites.title|Your well-loved pages.|Deine Lieblingsseiten.|Vos pages préférées.|Suas páginas favoritas.
favorites.sub|Recipes to come back to, again and again.|Rezepte, zu denen du gern zurückkehrst.|Des recettes à refaire avec plaisir.|Receitas para fazer de novo.
favorites.empty|A place for your favorites|Platz für deine Favoriten|Une place pour vos favoris|Um lugar para suas favoritas
favorites.empty.sub|Tap the heart on a recipe to keep it here.|Tippe im Rezept auf das Herz, um es hier zu speichern.|Touchez le cœur d’une recette pour la garder ici.|Toque no coração de uma receita para guardá-la aqui.
cloud.title|Your private iCloud|Deine private iCloud|Votre iCloud privé|Seu iCloud privado
cloud.toggle|Sync notes, favorites and plans|Notizen, Favoriten und Plan abgleichen|Synchroniser notes, favoris et programme|Sincronizar notas, favoritos e planos
cloud.help|Optional. Keep notes, favorites and your baking plan in your private iCloud storage. An Apple account with iCloud and available space is needed. Recipes and local changes stay available offline.|Optional. Bewahre Notizen, Favoriten und deinen Backplan in deinem privaten iCloud-Speicher auf. Dafür brauchst du ein Apple-Konto mit iCloud und freiem Speicherplatz. Rezepte und lokale Änderungen bleiben offline verfügbar.|Facultatif. Retrouvez notes, favoris et programme dans votre espace iCloud privé. Un compte Apple avec iCloud et de l’espace disponible est nécessaire. Les recettes et modifications locales restent accessibles hors ligne.|Opcional. Guarde notas, favoritos e o plano no seu iCloud privado. É preciso ter uma conta Apple com iCloud e espaço disponível. Receitas e alterações locais continuam acessíveis offline.
cloud.now|Sync now|Jetzt abgleichen|Synchroniser|Sincronizar agora
cloud.local|Saved on this device|Auf diesem Gerät gespeichert|Enregistré sur cet appareil|Salvo neste aparelho
cloud.syncing|Syncing with your private iCloud…|Abgleich mit deiner privaten iCloud…|Synchronisation avec votre iCloud privé…|Sincronizando com seu iCloud privado…
cloud.simulator|iCloud sync requires a signed device build. Local saving is active.|iCloud-Abgleich braucht eine signierte Geräteversion. Lokales Speichern ist aktiv.|La synchronisation iCloud nécessite une version signée sur appareil. L’enregistrement local est actif.|A sincronização exige uma versão assinada em aparelho. O salvamento local está ativo.
cloud.account|Sign into iCloud in system settings. Your changes are saved locally.|Melde dich in den Systemeinstellungen bei iCloud an. Änderungen sind lokal gespeichert.|Connectez-vous à iCloud dans les réglages. Vos modifications sont enregistrées ici.|Entre no iCloud nos ajustes do sistema. Suas alterações estão salvas localmente.
cloud.changed|iCloud account changed. Sync is off. Enable it again to merge local data with the new account.|iCloud-Konto geändert. Abgleich ist aus. Erneut aktivieren, um lokale Daten mit dem neuen Konto zusammenzuführen.|Compte iCloud modifié. Synchronisation désactivée. Réactivez-la pour fusionner les données avec le nouveau compte.|Conta do iCloud alterada. Sincronização desativada. Ative de novo para mesclar os dados com a nova conta.
cloud.synced|Your private iCloud is up to date|Deine private iCloud ist aktuell|Votre iCloud privé est à jour|Seu iCloud privado está atualizado
cloud.failed|iCloud is unavailable. Changes are safe here; retry when connected.|iCloud ist nicht verfügbar. Änderungen sind lokal sicher. Später erneut versuchen.|iCloud indisponible. Vos modifications sont conservées ici ; réessayez une fois connecté.|iCloud indisponível. Alterações salvas aqui; tente ao se conectar.
notifications|Local notifications|Lokale Mitteilungen|Notifications locales|Notificações locais
notification.value|Choose a gentle weekly nudge or seasonal inspiration. Alerts are scheduled on your device, with no server.|Wähle einen Wochenhinweis oder saisonale Ideen. Mitteilungen werden ohne Server auf deinem Gerät geplant.|Choisissez un rappel hebdomadaire ou saisonnier. Les alertes sont programmées sur cet appareil, sans serveur.|Escolha um aviso semanal ou inspiração sazonal. Os avisos são agendados no aparelho, sem servidor.
weekly.toggle|Sunday planning · 10:00|Sonntags planen · 10:00|Préparer le dimanche · 10:00|Planejar no domingo · 10:00
seasonal.toggle|New season · first day at 10:00|Neue Saison · erster Tag um 10:00|Nouvelle saison · premier jour à 10:00|Nova estação · primeiro dia às 10:00
system.settings|Open system settings|Systemeinstellungen öffnen|Ouvrir les réglages|Abrir ajustes do sistema
privacy|Privacy|Datenschutz|Confidentialité|Privacidade
privacy.body|No ads, purchases, analytics or tracking. Notes, favorites and plans stay on your device unless you enable private iCloud sync. Shopping and timers are shared only with your widgets. Reminder export uses Apple Reminders only when requested. No camera, microphone or location access.|Keine Werbung, Käufe, Analyse oder Tracking. Notizen, Favoriten und Pläne bleiben lokal, sofern du privaten iCloud-Abgleich nicht aktivierst. Einkaufsliste und Timer werden nur mit deinen Widgets geteilt. Erinnerungen werden nur auf Wunsch exportiert. Kein Zugriff auf Kamera, Mikrofon oder Standort.|Sans publicité, achat, analyse ni suivi. Notes, favoris et programme restent ici sauf si vous activez iCloud privé. Courses et minuteurs sont partagés uniquement avec vos widgets. L’export vers Rappels se fait à votre demande. Aucun accès caméra, micro ou localisation.|Sem anúncios, compras, análise ou rastreamento. Notas, favoritos e planos ficam no aparelho, salvo se ativar o iCloud privado. Compras e temporizadores são compartilhados só com seus widgets. A exportação para Lembretes ocorre quando solicitada. Sem câmera, microfone ou localização.
about|About|Über die App|À propos|Sobre
version|Version|Version|Version|Versão
about.body|A small, free cookbook for everyday home baking. Metric measures. A teaspoon is 5 ml; a tablespoon is 15 ml. Seasons follow the Northern Hemisphere calendar. Adjust cooking times to your oven.|Ein kleines kostenloses Backbuch. Metrische Maße. Ein TL hat 5 ml, ein EL 15 ml. Jahreszeiten nach dem Kalender der Nordhalbkugel. Backzeiten an deinen Ofen anpassen.|Un petit carnet de pâtisserie gratuit. Mesures métriques : cuillère à café de 5 ml, cuillère à soupe de 15 ml. Saisons de l’hémisphère nord. Adaptez les temps à votre four.|Um pequeno livro gratuito de confeitaria caseira. Medidas métricas: colher de chá de 5 ml, colher de sopa de 15 ml. Estações do Hemisfério Norte. Ajuste os tempos ao seu forno.
notification.error|The alert could not be scheduled. Your timer and plan are saved.|Mitteilung konnte nicht geplant werden. Timer und Plan sind gespeichert.|L’alerte n’a pas pu être programmée. Minuteur et programme sont enregistrés.|Não foi possível agendar o aviso. Seu temporizador e plano estão salvos.
notification.denied|Notifications are off. The timer and planner still work. You can enable alerts in system settings.|Mitteilungen sind aus. Timer und Plan funktionieren weiter. In den Systemeinstellungen aktivieren.|Notifications désactivées. Minuteur et programme fonctionnent. Activez les alertes dans les réglages.|Notificações desativadas. Temporizador e plano funcionam. Ative os avisos nos ajustes do sistema.
week.title|A little baking plan|Zeit für deinen Backplan|Un petit programme gourmand|Um plano mais doce
week.body|Choose something lovely to bake this week.|Wähle etwas Schönes zum Backen für diese Woche.|Choisissez une recette à préparer cette semaine.|Escolha uma receita para preparar nesta semana.
season.title|A new season in your kitchen|Neue Saison in deiner Küche|Une nouvelle saison en cuisine|Uma nova estação na cozinha
season.body|Explore the seasonal collection in Dessert Book.|Entdecke die saisonale Auswahl in Dessert Book.|Découvrez la sélection de saison dans Dessert Book.|Explore a coleção da estação no Dessert Book.
timer.exists|Finish or cancel your current timer first.|Aktuellen Timer zuerst abschließen oder beenden.|Terminez ou annulez d’abord le minuteur actuel.|Conclua ou cancele o temporizador atual primeiro.
live.unavailable|The timer is running. Live Activity is unavailable on this device.|Der Timer läuft. Live-Aktivität ist auf diesem Gerät nicht verfügbar.|Le minuteur fonctionne. L’activité en direct est indisponible sur cet appareil.|O temporizador está funcionando. Atividade ao Vivo indisponível neste aparelho.
reminder.denied|Reminders access was declined. Your baking plan is still saved here.|Zugriff auf Erinnerungen abgelehnt. Dein Backplan bleibt hier gespeichert.|Accès à Rappels refusé. Votre programme reste enregistré ici.|Acesso a Lembretes negado. Seu plano continua salvo aqui.
reminder.calendar|No writable Reminders list is available. Create one in Apple Reminders and try again.|Keine beschreibbare Erinnerungsliste vorhanden. Erstelle eine in Apple Erinnerungen.|Aucune liste Rappels accessible en écriture. Créez-en une dans Rappels et réessayez.|Nenhuma lista de Lembretes disponível. Crie uma no app Lembretes e tente de novo.
reminder.note|Planned in Dessert Book. Open the app for ingredients and steps.|In Dessert Book geplant. Zutaten und Schritte findest du in der App.|Programmé dans Dessert Book. Ouvrez l’app pour les ingrédients et étapes.|Planejado no Dessert Book. Abra o app para ver ingredientes e etapas.
reminder.saved|Saved in Apple Reminders.|In Apple Erinnerungen gespeichert.|Enregistré dans Rappels.|Salvo no app Lembretes.
reminder.error|The reminder could not be saved. Your plan is safe in Dessert Book.|Erinnerung konnte nicht gespeichert werden. Dein Plan ist in Dessert Book sicher.|Le rappel n’a pas pu être enregistré. Votre programme est conservé dans Dessert Book.|Não foi possível salvar o lembrete. Seu plano está salvo no Dessert Book.
bake|Baking|Backen|Pâtisserie|Preparo
widget.week|This week’s baking|Diese Backwoche|Les recettes de la semaine|Preparos da semana
widget.plan.empty|Choose your next recipes in the baking plan.|Wähle deine nächsten Rezepte im Backplan.|Choisissez vos prochaines recettes dans le programme.|Escolha suas próximas receitas no planejamento.
widget.shopping.empty|Add recipe ingredients in the app.|Füge Zutaten in der App hinzu.|Ajoutez les ingrédients depuis l’app.|Adicione ingredientes pelo app.
widget.name|Your kitchen page|Deine Küchenseite|Votre page cuisine|Sua página de cozinha
widget.description|A daily recipe, your oven timer and the next bakes. Always offline.|Tagesrezept, Backtimer und Backplan. Immer offline.|Recette du jour, minuteur et programme. Toujours hors ligne.|Receita do dia, temporizador e planejamento. Sempre offline.
timer.none|No active oven timer|Kein aktiver Backtimer|Aucun minuteur actif|Nenhum temporizador ativo
timer.short|Oven|Ofen|Four|Forno
g|g|g|g|g
ml|ml|ml|ml|ml
piece|pcs|Stk.|pce|un.
tsp|tsp|TL|c. à café|col. chá
tbsp|tbsp|EL|c. à soupe|col. sopa'''
# Use escaped newlines in the source table so one entry always occupies one line.
rows=rows.replace('Something sweet,\nmade by you.','Something sweet,\\nmade by you.').replace('Etwas Süßes,\nvon dir gemacht.','Etwas Süßes,\\nvon dir gemacht.').replace('Une douceur,\nfaite par vous.','Une douceur,\\nfaite par vous.').replace('Um doce,\nfeito por você.','Um doce,\\nfeito por você.')
strings={}
for row in rows.splitlines():
 a=row.split('|');assert len(a)==5,a
 strings[a[0]]={'localizations':{l:{'stringUnit':{'state':'translated','value':v.replace('\\n','\n')}} for l,v in zip(langs,a[1:])}}
if p.joinpath('Localizable.xcstrings').exists():
 old=json.loads(p.joinpath('Localizable.xcstrings').read_text())['strings']
 for k,v in old.items():
  if k not in strings: strings[k]=v
p.joinpath('Localizable.xcstrings').write_text(json.dumps({'sourceLanguage':'en','strings':strings,'version':'1.0'},ensure_ascii=False,indent=2))
privacy=['Dessert Book can add a planned bake to Apple Reminders when you choose to export it.','Dessert Book kann einen Backtermin auf deinen Wunsch in Apple Erinnerungen speichern.','Dessert Book peut ajouter une préparation à Rappels lorsque vous choisissez de l’exporter.','Dessert Book pode adicionar um preparo ao app Lembretes quando você escolher exportá-lo.']
keys=['NSRemindersUsageDescription','NSRemindersFullAccessUsageDescription']
s={k:{'localizations':{l:{'stringUnit':{'state':'translated','value':v}} for l,v in zip(langs,privacy)}} for k in keys}
s['CFBundleDisplayName']={'localizations':{l:{'stringUnit':{'state':'translated','value':'Dessert Book'}} for l in langs}}
p.joinpath('InfoPlist.xcstrings').write_text(json.dumps({'sourceLanguage':'en','strings':s,'version':'1.0'},ensure_ascii=False,indent=2))
