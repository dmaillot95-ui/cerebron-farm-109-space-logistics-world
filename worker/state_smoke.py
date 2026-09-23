import json,hashlib,pathlib
farm=109; cycle="SPACE-DEMO-0001"; seed=20260923
payload={"inventory_kg":900,"allocated_kg":600,"reserve_kg":300}
packet={"schema_version":"SPACE_STATE_V1","cycle_id":cycle,"producer":farm,"logical_time":farm-101,"seed":seed,"parent_sha":"GENESIS" if farm==101 else "UPSTREAM_REQUIRED_IN_E2E_V2","inputs_sha":"DEMO_INPUT","status":"PASS","epistemic":"REDUCED_DETERMINISTIC_SMOKE_NOT_PHYSICAL_VALIDATION","metrics":{},"events":[],"unknowns":["cross_repo_packet_transport_not_yet_connected"],"contradictions":[],"logistics_state":payload}
canonical=json.dumps(packet,sort_keys=True,separators=(",",":")).encode();packet["outputs_sha"]=hashlib.sha256(canonical).hexdigest();pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/state.json").write_text(json.dumps(packet,indent=2)+"\\n");print(json.dumps({"farm":farm,"cycle":cycle,"sha":packet["outputs_sha"],"status":"PASS"}))
