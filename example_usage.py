from client import HierarchicalCreatorTieringMatrixAllocatorClient

def main():
    client = HierarchicalCreatorTieringMatrixAllocatorClient()
    res = client.allocate_campaign_budget_tiers(50000.00)
    print('Tiering Matrix Allocator: ' + res['allocation_plan_id'] + ' (Budget: $' + str(res['budget_total_usd']) + ')')
    print('Projected Reach: ' + str(res['projected_total_reach']) + ' | Blended CPM: $' + str(res['blended_target_cpm_usd']))
    print('Schedule PDF: ' + res['allocation_schedule_pdf_url'])

if __name__ == '__main__':
    main()
