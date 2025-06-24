# Dm-Code

## 📖 Bot Commands

### `!dmall <message>`

Sends a **direct message (DM)** to **every non-bot member** of the server.

* ⚠️ Use responsibly — sending unsolicited mass DMs may violate Discord’s Terms of Service and result in your bot being banned.
* The bot must have permission to view members and send DMs.

**Example:**

```bash
!dmall Hello everyone! Please check the new updates in #announcements.
```

---

### `!dmrole <@role> <message>`

Sends a DM to **each member with a specified role**.

* Mention the role in the command (`@RoleName`).
* Bots are automatically skipped.

**Example:**

```bash
!dmrole @Helpers Don't forget the meeting at 5 PM today!
```

---

### `!dm <@user> <message>`

Sends a private message to a specific **user**.

* You can mention the user or use their ID.
* If the user has DMs disabled or blocked the bot, the message will fail.

**Example:**

```bash
!dm @JaneDoe Can you check the issue report?
```
