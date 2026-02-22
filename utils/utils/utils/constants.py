ITEMS_PER_PAGE = 10
BIG_WIN_THRESHOLD = 100
BIG_PURCHASE_THRESHOLD = 100
MAX_ROOMS = 20
MIN_PLAYERS = 2
MAX_PLAYERS = 5
MIN_BET = 3
MAX_COMPLETED_GIVEAWAYS = 10

SUPER_ADMINS = [int(x.strip()) for x in os.getenv("SUPER_ADMINS", "").split(",") if x.strip()]

PERMISSIONS_LIST = [
    "manage_users",
    "manage_shop",
    "manage_giveaways",
    "manage_channels",
    "manage_promocodes",
    "manage_tasks",
    "manage_chats",
    "manage_bosses",
    "manage_helpers",
    "manage_auctions",
    "manage_ads",
    "view_stats",
    "manage_bans",
    "broadcast",
    "cleanup",
    "edit_settings",
    "manage_admins",
    "manage_businesses",
    "manage_exchange",
    "manage_media",
]

DEFAULT_SETTINGS = {
    "random_attack_cost": "0",
    "targeted_attack_cost": "50",
    "theft_cooldown_minutes": "30",
    "theft_success_chance": "40",
    "theft_defense_chance": "20",
    "theft_defense_penalty": "10",
    "min_theft_amount": "5",
    "max_theft_amount": "15",
    "casino_win_chance": "40.0",
    "casino_min_bet": "1",
    "casino_max_bet": "1000",
    "casino_multiplier": "2.0",
    "dice_multiplier": "2.0",
    "dice_win_threshold": "7",
    "guess_multiplier": "5.0",
    "guess_reputation": "1",
    "slots_multiplier_three": "3.0",
    "slots_multiplier_diamond": "5.0",
    "slots_multiplier_seven": "10.0",
    "slots_win_probability": "25.0",
    "slots_min_bet": "1",
    "slots_max_bet": "500",
    "roulette_color_multiplier": "2.0",
    "roulette_green_multiplier": "18.0",
    "roulette_number_multiplier": "36.0",
    "roulette_min_bet": "1",
    "roulette_max_bet": "500",
    "multiplayer_min_bet": "5",
    "multiplayer_max_bet": "1000",
    "min_level_casino": "1",
    "min_level_dice": "1",
    "min_level_guess": "1",
    "min_level_slots": "3",
    "min_level_roulette": "5",
    "min_level_multiplayer": "7",
    "chat_notify_big_win": "1",
    "chat_notify_big_purchase": "1",
    "chat_notify_giveaway": "1",
    "gift_amount": "30",
    "gift_limit_per_day": "3",
    "gift_global_limit_per_user": "4",
    "gift_cooldown": "60",
    "referral_bonus": "50",
    "referral_reputation": "2",
    "referral_required_thefts": "15",
    "exp_per_casino_win": "2",
    "exp_per_casino_lose": "1",
    "exp_per_dice_win": "3",
    "exp_per_dice_lose": "1",
    "exp_per_guess_win": "4",
    "exp_per_guess_lose": "1",
    "exp_per_slots_win": "6",
    "exp_per_slots_lose": "2",
    "exp_per_roulette_win": "5",
    "exp_per_roulette_lose": "1",
    "exp_per_theft_success": "8",
    "exp_per_theft_fail": "2",
    "exp_per_theft_defense": "5",
    "exp_per_game_win": "12",
    "exp_per_game_lose": "3",
    "exp_per_fight": "5",
    "exp_per_smuggle": "10",
    "level_multiplier": "100",
    "level_reward_coins": "30",
    "level_reward_reputation": "3",
    "level_reward_coins_increment": "5",
    "level_reward_reputation_increment": "1",
    "reputation_theft_bonus": "0.5",
    "reputation_defense_bonus": "0.5",
    "reputation_smuggle_bonus": "0.2",
    "reputation_smuggle_success_bonus": "0.1",
    "reputation_max_bonus_percent": "30",
    "boss_spawn_chance": "20",
    "boss_min_interval": "360",
    "boss_max_per_day": "2",
    "boss_hp_multiplier": "200",
    "boss_attack_cooldown": "3",
    "boss_base_damage": "20",
    "boss_reward_coins": "500",
    "boss_reward_coins_variance": "200",
    "boss_reward_bitcoin": "10",
    "boss_reward_bitcoin_variance": "5",
    "stat_strength_per_level": "1",
    "stat_agility_per_level": "1",
    "stat_defense_per_level": "1",
    "auction_min_bid_step": "10",
    "auction_commission": "0",
    "auction_notify_chats": "1",
    "fight_cooldown_minutes": "30",
    "fight_base_damage": "5",
    "fight_damage_variance": "3",
    "fight_authority_min": "1",
    "fight_authority_max": "3",
    "fight_bitcoin_reward": "1",
    "gym_strength_cost": "10",
    "gym_agility_cost": "10",
    "gym_defense_cost": "10",
    "business_upgrade_cost_per_level": "10",
    "smuggle_min_duration": "30",
    "smuggle_max_duration": "120",
    "smuggle_success_chance": "55",
    "smuggle_caught_chance": "30",
    "smuggle_lost_chance": "15",
    "smuggle_base_amount": "8",
    "smuggle_authority_multiplier": "0.1",
    "smuggle_cooldown_minutes": "60",
    "smuggle_fail_penalty_minutes": "30",
    "bitcoin_per_theft": "1",
    "bitcoin_per_fight": "1",
    "bitcoin_per_casino_win": "2",
    "bitcoin_per_slots_win": "3",
    "bitcoin_per_roulette_win": "2",
    "bitcoin_per_dice_win": "1",
    "bitcoin_per_guess_win": "1",
    "bitcoin_per_boss_participation": "2",
    "exchange_min_price": "1",
    "exchange_max_price": "0",
    "exchange_commission_percent": "0",
    "exchange_commission_side": "seller",
    "exchange_commission_destination": "burn",
    "exchange_min_amount_btc": "0.001",
    "cleanup_days_fight_logs": "7",
    "cleanup_days_bosses": "7",
    "cleanup_days_auctions": "30",
    "cleanup_days_purchases": "30",
    "cleanup_days_giveaways": "30",
    "cleanup_days_user_tasks": "30",
    "cleanup_days_smuggle": "30",
    "cleanup_days_bitcoin_orders": "30",
    "auto_delete_commands_seconds": "30",
    "new_user_bonus": "50",
    "global_cooldown_seconds": "3",
    "max_input_number": "1000000",
}

BONUS_PHRASES = [
    "🎉 Отлично, лови +{bonus} баксов!",
    "💰 Ты сегодня богат! +{bonus} баксов!",
    "🌟 Удача улыбнулась! +{bonus} баксов в карман!",
    "🍀 Держи +{bonus} баксов на удачу!",
    "🎁 Поздравляю! +{bonus} баксов твои!"
]

CASINO_WIN_PHRASES = [
    "🎰 Ура! Ты выиграл {win} баксов (чистыми {profit})!",
    "🍒 Джекпот! +{profit} баксов!",
    "💫 Фортуна на твоей стороне! +{profit} баксов!",
    "🎲 Победа! {profit} баксов твои!",
    "✨ Ты обыграл казино! +{profit} баксов!"
]

CASINO_LOSE_PHRASES = [
    "😢 Обидно, потерял {loss} баксов.",
    "💔 Не повезло, минус {loss}.",
    "📉 Проигрыш -{loss} баксов.",
    "🍂 В следующий раз повезёт, а пока -{loss}.",
    "⚡️ Увы, -{loss} баксов."
]

PURCHASE_PHRASES = [
    "✅ Куплено! Админ скоро свяжется.",
    "🛒 Товар твой! Жди админа.",
    "🎁 Отличная покупка! Админ уже в курсе.",
    "💎 Приятной игры! Админ напишет."
]

DICE_WIN_PHRASES = [
    "🎲 {dice1} + {dice2} = {total} — Победа! +{profit} баксов!",
    "🎲 Круто! {dice1}+{dice2}={total}, ты выиграл {profit}!",
    "🎲 Хороший бросок! {total} очков, выигрыш {profit}!"
]

DICE_LOSE_PHRASES = [
    "🎲 {dice1} + {dice2} = {total} — Проигрыш. -{loss} баксов.",
    "🎲 Эх, {total} очков, не повезло. -{loss}.",
    "🎲 В следующий раз повезёт, -{loss} баксов."
]

GUESS_WIN_PHRASES = [
    "🔢 Ты угадал! Было {secret}. Выигрыш: +{profit} баксов и +{rep} репутации!",
    "🔢 Красава! Число {secret}, твой выигрыш {profit} баксов!",
    "🔢 Удача! +{profit} баксов, репутация +{rep}!"
]

GUESS_LOSE_PHRASES = [
    "🔢 Не угадал. Было {secret}. -{loss} баксов.",
    "🔢 Увы, загадано {secret}. Теряешь {loss} баксов.",
    "🔢 Не повезло, правильный ответ {secret}. -{loss}."
]

SLOTS_WIN_PHRASES = [
    "🍒 {combo} — Ура! Выигрыш x{multiplier}! +{profit} баксов!",
    "🍋 Джекпот! {combo} приносит {profit} баксов!",
    "🍊 Крутая комбинация! x{multiplier}, +{profit} баксов!",
    "💎 Бриллианты! Твой выигрыш: {profit} баксов!"
]

SLOTS_LOSE_PHRASES = [
    "🍒 {combo} — Не повезло. -{loss} баксов.",
    "🍋 Мимо. Потеряно {loss} баксов.",
    "🍊 В следующий раз повезёт. -{loss}."
]

ROULETTE_WIN_PHRASES = [
    "🎡 Выпало {number} {color}! Ты выиграл {profit} баксов!",
    "🎡 Удача! Ставка сыграла, +{profit} баксов!",
    "🎡 Круто! {profit} баксов твои!"
]

ROULETTE_LOSE_PHRASES = [
    "🎡 Выпало {number} {color}. Твоя ставка не сыграла. -{loss} баксов.",
    "🎡 Увы, не в этот раз. Потеряно {loss} баксов.",
    "🎡 Мимо кассы. -{loss}."
]

FIGHT_HIT_PHRASES = [
    "💥 Ты нанёс {damage} урона банде! Заработал {authority} авторитета.",
    "⚡️ Твой удар точный! +{damage} урона, +{authority} авторитета.",
    "🔥 Ты нанёс {damage} урона и получил {authority} авторитета.",
    "🤜 Хрясь! Банда получила {damage} урона. Твой авторитет +{authority}.",
    "👊 Смачный удар! {damage} урона, {authority} авторитета.",
]

FIGHT_CRIT_PHRASES = [
    "💢 СОКРУШИТЕЛЬНЫЙ УДАР! Ты нанёс {damage} урона (крит!) и заработал {authority} авторитета.",
    "🌟 Ты в ярости! Критический урон {damage}, авторитет +{authority}.",
    "⚡️ МОЛНИЕНОСНЫЙ ВЫПАД! {damage} урона, +{authority} авторитета.",
]

FIGHT_COUNTER_PHRASES = [
    "😵 Банда контратаковала! Ты потерял {damage} баксов и не получил авторитет.",
    "💥 Ответный удар! Ты потерял {damage} баксов.",
    "👊 Тебя самого ударили! Минус {damage} баксов.",
]

SMUGGLE_START_PHRASES = [
    "🛥 Ты отправился в контрабандный рейс! В этот раз груз – {cargo}. Вернёшься примерно {end_time}.",
    "📦 Груз загружен, судно вышло в море. Капитан обещает вернуться к {end_time}. Груз: {cargo}.",
    "🚤 Ты взял курс на нейтральные воды. На борту – {cargo}. Финиш ориентировочно {end_time}.",
    "⚓ Под покровом ночи ты вышел в море. Товар: {cargo}. Жди возвращения к {end_time}.",
]

SMUGGLE_CARGO = [
    "ящики с сигарами", "партия виски", "контрабандное оружие", "драгоценные камни",
    "золотые слитки", "антиквариат", "редкие лекарства", "элитный алкоголь",
    "техника без пошлин", "запрещённые книги", "экзотические животные", "наркотические вещества"
]

SMUGGLE_SUCCESS_PHRASES = [
    "✅ Рейс завершён успешно! Ты привёз {amount} BTC. Чёрный рынок доволен.",
    "💰 Товар сбыт с хорошей наценкой! +{amount} BTC осело в кармане.",
    "🎉 Пограничников удалось обмануть! Выручка: {amount} BTC.",
    "🚢 Корабль вернулся в порт, груз продан. Твоя доля: {amount} BTC.",
]

SMUGGLE_CAUGHT_PHRASES = [
    "🚨 Береговая охрана перехватила судно! Всё конфисковано. Ты в бегах.",
    "⛓ Полиция накрыла явочную квартиру. Придётся залечь на дно (кулдаун увеличен).",
    "👮‍♂️ Менты вышли на след. Контрабанда конфискована. Объявлен в розыск.",
    "🔫 Перестрелка с таможенниками! Пришлось бросить груз и спасаться бегством.",
]

SMUGGLE_LOST_PHRASES = [
    "🌊 Шторм уничтожил твоё судно! Груз утонул.",
    "💥 Корабль напоролся на рифы. Все ящики на дне.",
    "🔥 Двигатель взорвался. Придётся начинать сначала.",
    "🏝 Ты сел на мель на необитаемом острове. Спасся, но без груза.",
]

MULTIPLAYER_PHRASES = [
    "🎮 Комната {game_id} создана!",
    "👥 Игроки: {players}",
    "🎯 Твой ход!",
    "🏆 Победитель: {winner}",
]

BUSINESS_BUY_PHRASES = [
    "✅ Ты приобрёл бизнес «{name}»! Он будет приносить доход в баксах.",
    "🏪 Поздравляю с покупкой! Теперь у тебя есть {name}.",
]

BUSINESS_COLLECT_PHRASES = [
    "💰 Ты собрал {coins} баксов с бизнеса «{name}».",
    "💵 Прибыль от {name}: {coins} баксов.",
]

BUSINESS_NO_INCOME = [
    "⏳ В твоих бизнесах пока нет дохода. Загляни позже.",
]

GIVEAWAY_COMPLETED_PHRASE = [
    "🏁 Розыгрыш #{id} завершён! Победитель: {winner}",
    "🎉 Розыгрыш «{prize}» окончен! Список победителей: {winners}",
]

BOSS_SPAWN_PHRASES = [
    "⚠️ ВНИМАНИЕ! В чате появился {name} (Уровень {level})! Здоровье: {hp}",
    "👾 Босс {name} пришёл навестить нас! Уровень {level}, HP: {hp}",
    "🔥 Легендарный {name} пробудился! Уровень {level}, здоровье: {hp}",
]

BOSS_HIT_PHRASES = [
    "💥 Ты нанёс {damage} урона!",
    "⚡️ Удар! -{damage} HP",
    "🔥 Критическое попадание! {damage} урона",
]

BOSS_MISS_PHRASES = [
    "💨 Промах! Босс уклонился",
    "😵 Твоя атака не достигла цели",
    "🛡 Босс отразил удар",
]

BOSS_DEATH_PHRASES = [
    "🏆 Босс {name} повержен! Все участники получают награду!",
    "🎉 Победа! {name} пал! Награда разделена между участниками",
    "💀 Босс уничтожен! Спасибо за участие!",
]

BOSS_STATUS_PHRASES = [
    "👾 {name} | Уровень {level} | HP: {current_hp}/{max_hp}",
]

BOSS_ANGRY_PHRASES = [
    "Ты думал, что в нашем районе можно просто так ходить? Получи {damage} урона!",
    "Я закопаю тебя в пустыне! Держи {damage}!",
    "Ты подписал себе смертный приговор! Атака {damage}!",
    "Мои парни сейчас разберутся с тобой! {damage} урона!",
    "Ты пожалеешь, что связался с мафией! Получай {damage}!",
]

BOSS_HAPPY_PHRASES = [
    "Ха, слабак! Мой авторитет не пошатнуть! Осталось {hp_remaining} HP.",
    "Ты всего лишь муравей. У меня ещё {hp_remaining} здоровья!",
    "Мои люди скоро придут на помощь! HP: {hp_remaining}",
    "Я видал и не такое. HP осталось: {hp_remaining}",
]

THEFT_CHOICE_PHRASES = [
    "🔫 Выбери цель:",
    "💢 Кого будем грабить?",
    "😈 Куда направим бандитские лапы?"
]

THEFT_COOLDOWN_PHRASES = [
    "⏳ Ты ещё не остыл. Подожди {minutes} мин.",
    "🕐 Полегче! Отдохни {minutes} минут.",
    "😴 Слишком часто. Возвращайся через {minutes} мин."
]

THEFT_NO_MONEY_PHRASES = [
    "😕 У тебя нет баксов на подготовку к краже!",
    "💸 Сначала заработай!",
    "💰 Пустой карман – не до криминала."
]

THEFT_SUCCESS_PHRASES = [
    "🔫 Отлично! Ты украл {amount} баксов у {target}!",
    "💰 Хорошо пошло! {amount} баксов у {target} теперь твои!",
    "🦹‍♂️ Удачная кража! +{amount} баксов!",
    "😈 Ты невидимка! +{amount} баксов!"
]

THEFT_FAIL_PHRASES = [
    "😢 Облом, тебя спалили! Ничего не украл.",
    "🚨 {target} оказался бдительным!",
    "👮‍♂️ Пришлось сваливать, 0 баксов.",
    "💔 Не фортануло."
]

THEFT_DEFENSE_PHRASES = [
    "🛡️ {target} отразил атаку! Ты потерял {penalty} баксов.",
    "💥 Бабах! {target} выставил защиту, ты лишился {penalty} баксов.",
    "😱 Засада! Ты потерял {penalty} баксов."
]

THEFT_VICTIM_DEFENSE_PHRASES = [
    "🛡️ Твоя защита сработала! {attacker} ничего не украл и потерял {penalty} баксов.",
    "💪 Отлично! Отбил атаку {attacker} и получил {penalty} баксов.",
    "😎 Ха! {attacker} думал поживиться, а сам потерял {penalty} баксов."
]

CHAT_WIN_PHRASES = [
    "🔥 {name} только что выиграл {amount} баксов в казино!",
    "💰 Удача на стороне {name}: +{amount} баксов!",
    "🎰 {name} сорвал куш — {amount} баксов!"
]

CHAT_PURCHASE_PHRASES = [
    "🛒 {name} купил {item} за {price} баксов!",
    "🎁 {name} приобрёл {item}! Админ уже в пути.",
    "💎 {name} потратил {price} баксов на {item}!"
]

CHAT_GIVEAWAY_PHRASES = [
    "🎁 Не пропусти розыгрыш! Осталось {time}",
    "⏰ Напоминание: розыгрыш {prize} заканчивается через {time}",
    "🔥 Участвуй в розыгрыше {prize}! Осталось {time}"
]
