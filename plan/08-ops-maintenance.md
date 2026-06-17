# 08 — Operations & Maintenance

## Monitoring

- Uptime monitor (host or external)
- Core Web Vitals tracking
- Form-delivery monitoring (alert if submissions fail)
- SSL expiry alert (auto-renew, but verify)

## Updates

- Dependency updates (scheduled, tested via preview)
- CMS / framework version upgrades
- Periodic legal-content review (TBB rules can change — last major 09.08.2024)

## Content workflow (client)

1. Client logs into CMS
2. Drafts / edits article or page
3. Lawyer reviews for compliance (banned phrases, anonymization)
4. Publish → CI/CD auto-deploy
5. Verify live

## Handover / training

- Short CMS usage guide for non-technical client
- List of compliance do/don't (one-pager from `01`)
- Contacts: who to call for tech vs legal issues

## Recurring compliance audit

- Quarterly: re-run `01` pre-launch checklist on live site
- After any TBB regulation change: re-review content + keywords

## Ownership

| Area | Owner |
| --- | --- |
| Tech / hosting | Developer |
| Content | Firm |
| Legal compliance | Lawyer |
| CMS admin | Firm (trained) |
