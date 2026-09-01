class HierarchicalCreatorTieringMatrixAllocatorClient:
    def allocate_campaign_budget_tiers(self, total_campaign_budget_usd=100000.00, campaign_objective='FULL_FUNNEL_BRAND_AND_CONVERSION'):
        return {
            'allocation_plan_id': 'tier_alc_5519',
            'budget_total_usd': total_campaign_budget_usd,
            'tier_distribution': {
                'mega_macro_creators_count': 2,
                'mid_tier_creators_count': 8,
                'micro_nano_seed_creators_count': 35
            },
            'projected_total_reach': 4250000,
            'blended_target_cpm_usd': 23.50,
            'allocation_schedule_pdf_url': 'https://influencer.genpark.ai/allocations/5519.pdf'
        }
